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
- [Contributing](#contributing)
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
    ├── assets                                    # All media/data files
    │   └── Data                                  # Data files
    |       ├── accepted_2007_to_2018Q4.csv.gz    # Dataset of the Accepted loan in a compressed csv format
    |       └── rejected_2007_to_2018Q4.csv.gz    # Dataset of the Rejected loan in a compressed csv format
    ├── EDA and test script                       # Self explainatory
    |   ├── mlruns                                # Folder Containing the mlflow logging results i've made
    |   ├── DataExploration.ipynb                 # contains all the test for the models selection
    |   ├── ModelCreater.py                       # small script that uses the packages and the data to create a trained SGD Classifier model from it
    |   ├── ModelPred.ipynb                       # test script that helped me test my API laon prediciton 
    │   └── model_Pred_1.bin                      # model built by the ModelCreater, contains the                 
    ├── src                     # 
    ├── test                    # 
    ├── tools                   # 
    

    ├── benchmarks          # Load and stress tests
    │   ├── integration         # End-to-end, integration tests (alternatively `e2e`)
    │   └── unit 





main.py: FastAPI application.
Loan_Preprocess_and_Model_Trainer/: Package containing preprocessing and model training modules.
html/: Directory containing HTML templates for the web interface.
Pipfile and Pipfile.lock: Dependency files for managing Python dependencies.
Dockerfile: Docker configuration for containerization (optional).
### Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature: git checkout -b feature-yourfeature.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature-yourfeature.
Create a new Pull Request.
### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Special thanks to the FastAPI and scikit-learn communities for providing excellent tools for building and deploying machine learning applications.
Feel free to add your own acknowledgments and contributors here.
arduino
