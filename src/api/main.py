from fastapi import FastAPI


from src.predictionModels.ModelPred import predict_loan_acceptation

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI-powered API!"}

@app.get("/predict")
async def predict():
    result = predict_loan_acceptation()  # Call a function from the 'modelPred' module
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9696)

