#!/usr/bin/env python
# coding: utf-8



import pickle
import numpy as np
import pandas as pd
import json 
from flask import Flask , request , jsonify


import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(script_dir, 'model_Pred_1.bin')

with open(model_file_path, 'rb') as f_in:
    (scaler, numerical_imputer, model) = pickle.load(f_in)


def Dataformater(data):

    

     # Extract and assign values to variables
    x1 = data.get("Amount Requested")
    x2 = data.get("Debt-To-Income Ratio")
    x3 = data.get("employment Length")
    x4 = data.get("policy_code")
    x5 = data.get("risk_score")

    # Check and set "missing" variables accordingly
    def set_missing_variable(value):
        return 1 if pd.isna(value) or value is None else 0

    x6 = set_missing_variable(x1)
    x7 = set_missing_variable(x2)
    x8 = set_missing_variable(x3)
    x9 = set_missing_variable(x4)
    x10 = set_missing_variable(x5)

    # Create a list containing all the features that need imputation
    features_to_impute = [x1, x2, x3, x4, x5]

    # Use the numerical imputer to fill missing values for all features at once
    features_to_impute = numerical_imputer.transform([features_to_impute])[0]

    # Update the individual variables
    x1, x2, x3, x4, x5 = features_to_impute

    # Create a numpy array from the extracted values
    loan_client_info = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10])

    # Reshape the array for further processing (if needed)
    loan_client_info = loan_client_info.reshape(1, -1)

    # Return the formatted data (assuming you have the 'scaler' defined elsewhere)
    return scaler.transform(loan_client_info)




app = Flask("predLoan")



                 

@app.route('/predict',methods=['POST'])
def predict():

    json_loan_client_info = request.get_json()
    
    
    pred = model.predict(Dataformater(json_loan_client_info))
    result = {
        'accepted_pred':pred.tolist()
    }

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port =9696)


