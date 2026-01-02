# ============================================
# STUDENT PERFORMANCE PREDICTOR - Backend API
# ============================================
# This file creates a simple API that predicts
# a student's exam score based on study hours
# and attendance percentage.
# ============================================

# Import FastAPI to create our web API
from fastapi import FastAPI
# Import CORS so our HTML page can talk to this API
from fastapi.middleware.cors import CORSMiddleware
# Import Pydantic to define what data we expect
from pydantic import BaseModel

# Create our FastAPI application
app = FastAPI()

# Allow our HTML pages to connect to this API
# (This is called CORS - Cross Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all websites to connect
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ============================================
# TRAINING DATA (Simple examples to learn from)
# ============================================
# This is fake data that represents past students
# Format: (study_hours, attendance_percent, exam_score)
training_data = [
    (1, 30, 25),   # Student who barely studied, got 25%
    (2, 40, 35),   # Student with low effort, got 35%
    (3, 50, 45),   # Average student, got 45%
    (4, 60, 55),   # Decent student, got 55%
    (5, 70, 65),   # Good student, got 65%
    (6, 75, 72),   # Very good student, got 72%
    (7, 80, 78),   # Great student, got 78%
    (8, 85, 85),   # Excellent student, got 85%
    (9, 90, 92),   # Outstanding student, got 92%
    (10, 95, 98),  # Perfect student, got 98%
]

# ============================================
# Define what data we expect from the user
# ============================================
class StudentInput(BaseModel):
    study_hours: float      # How many hours student studies daily
    attendance: float       # Attendance percentage (0-100)


# ============================================
# Simple prediction formula
# ============================================
def predict_score(study_hours, attendance):
    """
    This function predicts exam score using a simple formula.
    
    The idea is simple:
    - More study hours = better score
    - Higher attendance = better score
    
    Formula breakdown:
    - study_hours * 5 = Each hour of study adds 5 points (max 50 from 10 hours)
    - attendance * 0.5 = Attendance contributes half its value (max 50 from 100%)
    - Together they can give max 100 points
    """
    
    # Calculate score from study hours (multiply by 5)
    study_contribution = study_hours * 5
    
    # Calculate score from attendance (multiply by 0.5)
    attendance_contribution = attendance * 0.5
    
    # Add them together for total predicted score
    predicted_score = study_contribution + attendance_contribution
    
    # Make sure score doesn't go above 100 or below 0
    if predicted_score > 100:
        predicted_score = 100
    if predicted_score < 0:
        predicted_score = 0
    
    return round(predicted_score, 1)  # Round to 1 decimal place


def get_risk_level(score):
    """
    This function tells us if the student is at risk of failing.
    
    Simple rules:
    - Below 40 = High Risk (might fail)
    - 40 to 60 = Medium Risk (needs improvement)
    - Above 60 = Low Risk (doing well)
    """
    if score < 40:
        return "HIGH RISK - Student may fail!"
    elif score < 60:
        return "MEDIUM RISK - Needs to study more"
    else:
        return "LOW RISK - Student is doing well"


# ============================================
# API Endpoint - This is what the HTML calls
# ============================================
@app.post("/predict")
def predict_student_performance(data: StudentInput):
    """
    This function receives student data and returns prediction.
    
    Steps:
    1. Get study_hours and attendance from the request
    2. Calculate predicted score using our formula
    3. Determine risk level based on score
    4. Send back the results as JSON
    """
    
    # Step 1: Get the input values
    study_hours = data.study_hours
    attendance = data.attendance
    
    # Step 2: Calculate predicted score
    predicted_score = predict_score(study_hours, attendance)
    
    # Step 3: Determine risk level
    risk_level = get_risk_level(predicted_score)
    
    # Step 4: Return the results
    return {
        "predicted_score": predicted_score,
        "risk_level": risk_level,
        "study_hours": study_hours,
        "attendance": attendance,
        "message": f"Based on {study_hours} hours of study and {attendance}% attendance"
    }


# ============================================
# Health check endpoint (to test if API is running)
# ============================================
@app.get("/")
def home():
    """Simple endpoint to check if the API is working"""
    return {"message": "Student Performance Predictor API is running!"}
