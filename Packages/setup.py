from setuptools import setup, find_packages

setup(
    name="Loan_Preprocess_and_Model_Trainer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "mlflow",
        
    ],
)
