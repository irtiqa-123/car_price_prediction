from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import joblib

app = FastAPI()

# Mount static folder for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# Load trained model
model = joblib.load("models/linear_regression_model.pkl")

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict_price(request: Request,
                  year: int = Form(...),
                  mileage: float = Form(...),
                  brand: str = Form(...),
                  fuel_type: str = Form(...)):

    # Create input DataFrame
    input_df = pd.DataFrame([{
        "year": year,
        "mileage": mileage,
        "brand": brand,
        "fuel_type": fuel_type
    }])

    # One-hot encode categorical features
    categorical_cols = ["brand", "fuel_type"]
    input_encoded = pd.get_dummies(input_df, columns=categorical_cols)

    # Align input with model features
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_features]

    # Predict
    prediction = model.predict(input_encoded)[0]  # get scalar
    prediction = float(prediction)  # convert to Python float

    return templates.TemplateResponse("index.html", {
    "request": request,
    "prediction": f"₹ {round(prediction, 2):,.0f}"  # formatted with commas
})
