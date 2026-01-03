from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model
model = joblib.load("retail_model.joblib")

app = FastAPI(
    title="Retail Sales Prediction API",
    description="FastAPI app deployed on Render",
    version="1.0"
)

class SalesInput(BaseModel):
    customers: int
    stores: int
    products: int
    discount: int
    day: int
    month: int

@app.get("/")
def home():
    return {"message": "Retail Sales Prediction API running"}

@app.post("/predict")
def predict_sales(data: SalesInput):

    input_df = pd.DataFrame([{
        "customers": data.customers,
        "stores": data.stores,
        "products": data.products,
        "discount": data.discount,
        "day": data.day,
        "month": data.month
    }])

    prediction = model.predict(input_df)[0]

    return {"predicted_sales": round(float(prediction), 2)}
