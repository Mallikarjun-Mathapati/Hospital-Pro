# ============================================
# HOSPITAL PATIENT RISK CHECKER - Backend API
# ============================================
# This file creates a simple API that checks
# a patient's health risk level based on
# age, blood pressure, and sugar level.
# NOTE: This is for EDUCATIONAL purposes only!
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all websites to connect
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# ============================================
# TRAINING DATA (Simple examples to learn from)
# ============================================
# This is fake data representing different patients
# Format: (age, blood_pressure, sugar_level, risk_category)
# Risk categories: "Low", "Medium", "High"
training_data = [
    (25, 110, 90, "Low"),      # Young, normal BP and sugar
    (30, 115, 95, "Low"),      # Young adult, healthy
    (35, 120, 100, "Low"),     # Adult, normal readings
    (40, 125, 110, "Medium"),  # Middle age, slightly elevated
    (45, 130, 120, "Medium"),  # Middle age, elevated
    (50, 140, 130, "Medium"),  # Older, high BP
    (55, 150, 140, "High"),    # Senior, very high BP
    (60, 160, 150, "High"),    # Senior, dangerous levels
    (65, 170, 160, "High"),    # Elderly, very high risk
    (70, 180, 180, "High"),    # Elderly, critical levels
]

# ============================================
# Define what data we expect from the user
# ============================================
class PatientInput(BaseModel):
    age: int                # Patient's age in years
    blood_pressure: int     # Systolic blood pressure (top number)
    sugar_level: int        # Fasting blood sugar level


# ============================================
# Simple risk calculation functions
# ============================================
def calculate_age_risk(age):
    """
    Calculate risk points based on age.
    
    Simple logic:
    - Under 30: Low risk (0 points)
    - 30-50: Medium risk (1 point)
    - Over 50: Higher risk (2 points)
    """
    if age < 30:
        return 0  # Young people generally have lower risk
    elif age < 50:
        return 1  # Middle age has some risk
    else:
        return 2  # Older age has more risk


def calculate_bp_risk(blood_pressure):
    """
    Calculate risk points based on blood pressure.
    
    Normal BP is around 120 mmHg
    - Under 120: Normal (0 points)
    - 120-140: Elevated (1 point)
    - Over 140: High (2 points)
    """
    if blood_pressure < 120:
        return 0  # Normal blood pressure
    elif blood_pressure < 140:
        return 1  # Slightly high
    else:
        return 2  # High blood pressure


def calculate_sugar_risk(sugar_level):
    """
    Calculate risk points based on fasting sugar level.
    
    Normal fasting sugar is under 100 mg/dL
    - Under 100: Normal (0 points)
    - 100-125: Pre-diabetic (1 point)
    - Over 125: Diabetic range (2 points)
    """
    if sugar_level < 100:
        return 0  # Normal sugar level
    elif sugar_level < 126:
        return 1  # Pre-diabetic range
    else:
        return 2  # Diabetic range


def get_overall_risk(total_risk_points):
    """
    Determine overall risk level from total points.
    
    We add up all risk points (max possible = 6)
    - 0-2 points: Low Risk
    - 3-4 points: Medium Risk
    - 5-6 points: High Risk
    """
    if total_risk_points <= 2:
        return "LOW RISK"
    elif total_risk_points <= 4:
        return "MEDIUM RISK"
    else:
        return "HIGH RISK"


def get_health_advice(risk_level):
    """
    Give simple health advice based on risk level.
    """
    if risk_level == "LOW RISK":
        return "Great! Keep maintaining a healthy lifestyle."
    elif risk_level == "MEDIUM RISK":
        return "Consider regular checkups and lifestyle improvements."
    else:
        return "Please consult a doctor for proper medical advice."


# ============================================
# API Endpoint - This is what the HTML calls
# ============================================
@app.post("/check-risk")
def check_patient_risk(data: PatientInput):
    """
    This function receives patient data and returns risk assessment.
    
    Steps:
    1. Get age, blood_pressure, sugar_level from request
    2. Calculate risk points for each factor
    3. Add up total risk points
    4. Determine overall risk level
    5. Send back the results as JSON
    """
    
    # Step 1: Get the input values
    age = data.age
    blood_pressure = data.blood_pressure
    sugar_level = data.sugar_level
    
    # Step 2: Calculate individual risk points
    age_risk = calculate_age_risk(age)
    bp_risk = calculate_bp_risk(blood_pressure)
    sugar_risk = calculate_sugar_risk(sugar_level)
    
    # Step 3: Add up total risk points
    total_risk = age_risk + bp_risk + sugar_risk
    
    # Step 4: Determine overall risk level
    risk_level = get_overall_risk(total_risk)
    
    # Get health advice
    advice = get_health_advice(risk_level)
    
    # Step 5: Return the results
    return {
        "risk_level": risk_level,
        "total_risk_points": total_risk,
        "max_possible_points": 6,
        "breakdown": {
            "age_risk": age_risk,
            "bp_risk": bp_risk,
            "sugar_risk": sugar_risk
        },
        "advice": advice,
        "disclaimer": "This is for EDUCATIONAL purposes only. Always consult a real doctor!"
    }


# ============================================
# Health check endpoint (to test if API is running)
# ============================================
@app.get("/")
def home():
    """Simple endpoint to check if the API is working"""
    return {"message": "Patient Risk Checker API is running!"}
