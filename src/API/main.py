from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Assuming "main.py" is located in the "api" directory
html_dir = Path(__file__).resolve().parent / "html"

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
     amount: str = Form(None),
    debt: str = Form(None),
    employment: str = Form(None),
    policy: str = Form(None),
    score: str = Form(None),
):
     # Helper function to clean and parse input fields
    def clean_and_parse(input_str):
        if input_str is None:
            return None
        return float(input_str.replace(" ", ""))

    # Clean and parse input fields
    amount = clean_and_parse(amount)
    debt = clean_and_parse(debt)
    employment = clean_and_parse(employment)
    policy = clean_and_parse(policy)
    score = clean_and_parse(score)

        
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

