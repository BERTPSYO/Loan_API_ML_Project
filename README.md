# Loan Prediction API

![GitHub repo size](https://img.shields.io/github/repo-size/BERTPSYO/Loan_API_ML_Project)
![GitHub stars](https://img.shields.io/github/stars/BERTPSYO/Loan_API_ML_Project?style=social)
![GitHub forks](https://img.shields.io/github/forks/BERTPSYO/Loan_API_ML_Project?style=social)

## Description

This repository contains an API for loan approval prediction. It uses a machine learning model to predict whether a loan application should be accepted or rejected. The project also includes preprocessing and model training modules. The API allows users to input various loan application parameters and receive a prediction.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

Before running the API, make sure you have the following prerequisites installed:

- Docker (tested on Docker Desktop)
- Windows (Use .Bat file to run the API, but should work on other system)
- Python 3.10 (Tested on Python 3.10.6, can normally work on other system)
- Other configuration might work (with maybe a little bit of work) but aren't tested.


### Installation

1. Clone the repository:
   
   git clone https://github.com/BERTPSYO/Loan_API_ML_Project.git

2. Install the Modules (Optionnal : used for Creating/Updating a new Model in the case there's aditionnal Data):
  
  Go to Packages, open a console and type : pip install .
  
3. Run the "run_api.Bat" to create the Docker Image, create the Container and Start the API
  

The API will be accessible at http://localhost:9696.

### Usage
Visit the main page of the API by opening your web browser and navigating to http://localhost:9696.

For now, There's only one program available: "The Loan Approval Prediction" used to determine if a loan would be accepted or declined based on previous loan approval and rejection.
You can use the loan prediction form to input various loan application parameters, such as the amount requested, debt-to-income ratio, employment length, policy code, and risk score.
Click "Submit" to get a prediction result, which will display whether the loan should be accepted or rejected.
### Project Structure
The project structure is organized as follows:



    .   
    ├── EDA and test script                       # Self explainatory
    |   |
    |   ├── mlruns                                # Folder Containing the mlflow logging results i've made
    |   ├── DataExploration.ipynb                 # contains all the test for the models selection
    |   ├── ModelCreater.py                       # small script that uses the packages and the data to create a trained SGD Classifier model from it
    |   ├── ModelPred.ipynb                       # test script that helped me test my API laon prediciton 
    │   └── model_Pred_1.bin                      # model built by the ModelCreater, contains the trained model, standard scaler, and numerical imputer              
    |
    ├── Packages                                  # List of package not contained in the API docker container, can be installed
    |   |
    |   ├── Loan_Preprocess_and_Model_Trainer     # Package #1 Contains a data preprocessing script and a model training script
    |   |   |
    |   |   ├── Model_Trainer.py                  # python script to train, test and log models
    |   |   ├── Preprocessing.py                  # python script to preprocess the data for the models
    |   |   └── __init__.py                       # To make this directory a package
    |   |
    |   └── Setup.py                              # To install this package
    |   
    ├── assets                                    # All media/data files
    |   |
    │   └── Data                                  # Data files
    |       |
    |       ├── accepted_2007_to_2018Q4.csv.gz    # Dataset of the Accepted loan in a compressed csv format
    |       └── rejected_2007_to_2018Q4.csv.gz    # Dataset of the Rejected loan in a compressed csv format
    |
    ├── src                                       # API source code
    |   |
    |   ├── API                                   # Main API directory
    |   |   |
    |   |   ├── html                              # list of HTML pages
    |   |   |   |
    |   |   |   ├── loan_prediction.html          # HTML pages with input field to make the loan prediction
    |   |   |   └── main.html                     # Main Landing Page
    |   |   |
    |   |   └── main.py                           # API main python script
    |   |
    |   └── predictionModels                      # First API microservices
    |       |
    |       ├── ModelPred.py                      # get data in input and return the predicition using the trained model
    |       ├── __init__.py                       # To make this directory a package loaded inside the docker
    |       └── model_Pred_1.bin                  # Trained model
    |
    ├── .gitattributes                            # Self explainatory
    ├── .gitignore                                # Self explainatory
    ├── Dockerfile                                # Docker config file
    ├── LICENSE                                   # Self explainatory
    ├── Pipfile                                   # managing docker depedencies
    ├── Pipfile.lock                              # managing docker depedencies
    ├── README.md                                 # this file
    └── run_api.bat                               # Bat file to create the docker image, start the container and run the API
    
    
### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Special thanks to the FastAPI and scikit-learn communities for providing excellent tools for building and deploying machine learning applications.
Feel free to add your own acknowledgments and contributors here.

