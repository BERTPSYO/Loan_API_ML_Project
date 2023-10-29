
import pandas as pd
import pickle

from Loan_Preprocess_and_Model_Trainer import Preprocessing , Model_Trainer




def main():

    df_accepted = pd.read_csv('../assets/data/accepted_2007_to_2018Q4.csv.gz', compression='gzip', header=0, sep=',', quotechar='\"')
        
    df_rejected = pd.read_csv('../assets/data/rejected_2007_to_2018Q4.csv.gz', compression='gzip', header=0, sep=',', quotechar='\"')



    scaler, numerical_imputer, preprocessed_DataSet = Preprocessing.DataPreprocessing(df_accepted , df_rejected)




    X_train = preprocessed_DataSet[0]
    X_test = preprocessed_DataSet[1]
    y_train = preprocessed_DataSet[2]
    y_test = preprocessed_DataSet[3]


    model = Model_Trainer.Train_SGD_Classifier(X_train,y_train)

    Model_Trainer.Test_SGD_Classifier(model, X_test , y_test)

    output_file = f'model_Pred_1.bin'

    with open(output_file, 'wb') as f_out :
        pickle.dump((scaler,numerical_imputer, model), f_out)


main()
