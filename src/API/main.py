from fastapi import FastAPI
import sys
sys.path.insert(0, "D:\\Users\\Bertr\\OneDrive\\Yohann\\Projet ML\\Loan_API_ML_Project\\src\\predictionModels")

from ModelPred import app as model_loan_pred_app  # Import a module with specific functionality

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI-powered API!"}

@app.get("/predict")
async def predict():
    result = model_loan_pred_app.predict_loan_acceptation()  # Call a function from the 'prediction' module
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9696)

