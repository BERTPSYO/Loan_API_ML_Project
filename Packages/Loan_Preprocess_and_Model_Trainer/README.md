# Loan Package
## Overview
This package provides functionalities for loan data processing, model training, and testing. It is designed to work seamlessly with machine learning models for loan acceptance prediction.

## Functions
### Script 1: Model Training and Testing
#### Train_SGD_Classifier(X_train, y_train)
Train a SGD Classifier from the training dataset.

- Log the result in Mlflow.
- Return the trained model.

#### Test_SGD_Classifier(model, X_test, y_test)
- Test the SGD Classifier model with the test dataset.

- Log the accuracy_score, roc_auc_score, and a confusion matrix of the result in Mlflow.

### Script 2: Data Preprocessing
#### DataPreprocessing(df_accepted, df_rejected)
- Get two CSV.GZ data files and preprocess the data.

- Drop unnecessary columns from the accepted loans DataFrame.
- Create a risk score for the accepted DataFrame.
- Combine accepted and rejected DataFrames.
- Reset the index for the combined DataFrame.
- Drop non-numeric columns.
- Create indicator columns for each column with missing values.
- Clean specified columns (Debt-To-Income Ratio, Employment Length).
- Impute missing values with the mean for numerical columns.
- Shuffle and scale the data.
- Return the Standard scaler, the numerical imputer used, and the preprocessed data as an array [X_train, X_test, y_train, y_test].

#### Additional Functions
#### P2f(x)
Remove the percent "%" symbol from a string and return a float. Return NaN if the string is empty.

#### Stringremover(x)
Remove any non-numerical character from a string. Return NaN if the string is empty.

## Usage
To use this package, follow these steps:

1. Install the required dependencies by running:
`poetry install`
2. Run the desired scripts:

- For Model Training and Testing:
```
# Import required functions
from Loan_Preprocess_and_Model_Trainer import Train_SGD_Classifier, Test_SGD_Classifier

# Replace X_train, y_train, X_test, y_test with your actual data
model = Train_SGD_Classifier(X_train, y_train)
Test_SGD_Classifier(model, X_test, y_test)
```
For Data Preprocessing:

```
# Import required functions
from Loan_Preprocess_and_Model_Trainer import DataPreprocessing

# Replace df_accepted, df_rejected with your actual DataFrames
scaler, numerical_imputer, preprocessed_DataSet = DataPreprocessing(df_accepted, df_rejected)
```

You can see an example of it in the tests folder where I have a ModelCreater.py script that use both of these function to build a model from the DataSet and log the mlflow parameters into a mlruns folder.



## Dependencies
- pandas
- numpy
- scikit-learn
- mlflow
