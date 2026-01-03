from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model
model = joblib.load("student_model.joblib")

app = FastAPI(
    title="Student Performance Prediction API",
    description="Predict student final score based on study, attendance, and participation",
    version="1.0"
)

# Input schema
class StudentInput(BaseModel):
    study_hours: float
    attendance: float
    previous_grade: float
    assignments_completed: int
    participation: int

@app.get("/")
def home():
    return {"message": "Student Performance Prediction API running"}

@app.post("/predict")
def predict_student_score(data: StudentInput):
    input_df = pd.DataFrame([{
        "study_hours": data.study_hours,
        "attendance": data.attendance,
        "previous_grade": data.previous_grade,
        "assignments_completed": data.assignments_completed,
        "participation": data.participation
    }])
    prediction = model.predict(input_df)[0]
    return {"predicted_final_score": round(float(prediction), 2)}
