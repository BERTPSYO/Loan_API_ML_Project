from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

# Assuming "main.py" is located in the "api" directory
html_dir = os.path.join(os.path.dirname(__file__), "html")

from src.predictionModels.ModelPred import predict_loan_acceptation

app = FastAPI()

# Mount the "html" directory to serve static files like CSS or images
app.mount("/static", StaticFiles(directory=html_dir), name="static")

templates = Jinja2Templates(directory=html_dir)

# Main page
@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

# Loan Approval Prediction page
@app.get("/loan-prediction", response_class=HTMLResponse)
async def read_loan_prediction(request: Request):
    return templates.TemplateResponse("loan_prediction.html", {"request": request})

# Handle form submission
@app.post("/predict")
async def predict(request: Request,
    amount: float = Form(None),
    debt: float = Form(None),
    employment: float = Form(None),
    policy: float = Form(None),
    score: float = Form(None),
):
    # Handle form submission and prediction here
    # Convert empty values to None
    if amount == "":
        amount = None
    if debt == "":
        debt = None
    if employment == "":
        employment = None
    if policy == "":
        policy = None
    if score == "":
        score = None
    input_data = {
        "Amount Requested": amount,
        "Debt-To-Income Ratio": debt,
        "employment Length": employment,
        "policy_code": policy,
        "risk_score": score,
    }
    prediction = predict_loan_acceptation(input_data)

    return templates.TemplateResponse("loan_prediction.html", {"request": request, "prediction": prediction})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9696)

