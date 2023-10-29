#importing the necesary libraires
import pandas as pd
import re
import numpy as np

from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


from sklearn.impute import SimpleImputer









def DataPreprocessing(df_accepted , df_rejected):
    """
    Get the two csv.gz data file and preprocess the data.

    

    :param arg1: DataFrame of all the accepted Loan
    :type arg1: Pandas DataFrame

    :param arg2: DataFrame of all the rejected Loan
    :type arg2: Pandas DataFrame

    :return: Return the Standard scaler and the numerical imputer used and
     the Preprocessed Data as an array [X_train,X_test,y_train,y_test]
     
    :rtype: StandardScaler , SimpleImputer , array
    """
    
    #dropping the accepted loans additionnal columns as they are not neede to train or loans acceptability model
    df_accepted_clean = df_accepted[['loan_amnt','issue_d','title','dti','zip_code','addr_state','emp_length','policy_code']].copy()
    #making the risk Score for the accepted DataFrame
    df_accepted_clean['risk_score'] = df_accepted[['fico_range_low','fico_range_high']].mean(axis=1)


    ###combining the data###


    # Add the 'accepted' column to both dataframes
    df_accepted_clean['accepted'] = 1
    df_rejected['accepted'] = 0

    # Rename the columns in the Rejected dataframe to match the column names in the Accepted dataframe and vice-versa
    df_rejected = df_rejected.rename(columns={'Loan Title': 'title',
                                              'Policy Code': 'policy_code',
                                              'Risk_Score': 'risk_score'})
    df_accepted_clean = df_accepted_clean.rename(columns={'loan_amnt': 'Amount Requested',
                                              'issue_d': 'Application Date',                                          
                                              'dti': 'Debt-To-Income Ratio',
                                              'zip_code': 'Zip Code',
                                              'addr_state': 'State',
                                              'emp_length': 'Employment Length'})


    # Concatenate the dataframes vertically
    df_combined = pd.concat([df_accepted_clean, df_rejected], ignore_index=True)

    # reset the index to have a clean index for the combined dataframe
    df_combined.reset_index(drop=True, inplace=True)

    #droping the non-numeric columns
    df_combined = df_combined.drop(columns=['Application Date', 'title', 'Zip Code', 'State'])

    #create a new column to keep track of the null value for each columns since i presume missing value is really important in loan decision
    #clean the non numeric value in Debt-To-Income Ratio and Employment Length columns




    # Define a list of columns with missing values
    columns_with_missing_values = ['Amount Requested', 'Debt-To-Income Ratio', 'Employment Length', 'policy_code', 'risk_score']

    # Create indicator columns for each column with missing values and clean the specified columns
    for column in columns_with_missing_values:
        indicator_column_name = f'missing_{column}'
        df_combined[indicator_column_name] = df_combined[column].isnull().astype(int)

        # Apply data cleaning functions for specific columns
        if column == 'Debt-To-Income Ratio':
            df_combined[column] = df_combined[column].apply(lambda x: P2f(x) if pd.notna(x) else np.NaN)
        elif column == 'Employment Length':
            df_combined[column] = df_combined[column].apply(lambda x: Stringremover(x) if pd.notna(x) else np.NaN)


    # Impute missing values with the mean for numerical columns
    numerical_imputer = SimpleImputer(strategy='mean')
    df_combined[columns_with_missing_values] = numerical_imputer.fit_transform(df_combined[columns_with_missing_values])


    #separating and sacling the data
    df_combined = shuffle(df_combined)

    X_train, X_test, y_train, y_test = train_test_split(df_combined.loc[:,df_combined.columns != 'accepted'], df_combined['accepted'], test_size=0.25, random_state=1)
    

    # Standard scaling 
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    

    preprocessed_DataSet = [X_train,X_test,y_train,y_test]


    return scaler, numerical_imputer, preprocessed_DataSet









def P2f(x):
    if pd.notna(x) and not isinstance(x, float):
        return float(x.strip('%'))
    return np.NaN


    
def Stringremover(x):
    if pd.notna(x) and not x == "":
        return re.sub("[^0-9]", "", str(x))
    return np.NaN




