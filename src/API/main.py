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

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict_loan(
    request: Request,
    amount: int = Form(...),
    debt: int = Form(...),
    employment: int = Form(...),
    policy: int = Form(...),
    score: int = Form(...),
):
    input_data = {
        "Amount Requested": amount,
        "Debt-To-Income Ratio": debt,
        "employment Length": employment,
        "policy_code": policy,
        "risk_score": score,
    }
    prediction = predict_loan_acceptation(input_data)

    return templates.TemplateResponse("result.html", {"request": request, "prediction": prediction})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9696)

