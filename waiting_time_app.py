# ============================================
# HOSPITAL WAITING TIME ESTIMATOR - Backend API
# ============================================
# This file creates a simple API that predicts
# how long a patient will wait based on how
# many patients are already in the queue.
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
# This is fake data from past observations
# Format: (patients_in_queue, waiting_time_minutes)
training_data = [
    (0, 0),     # No queue, no wait
    (1, 8),     # 1 patient ahead, ~8 min wait
    (2, 15),    # 2 patients ahead, ~15 min wait
    (3, 22),    # 3 patients ahead, ~22 min wait
    (5, 35),    # 5 patients ahead, ~35 min wait
    (7, 50),    # 7 patients ahead, ~50 min wait
    (10, 70),   # 10 patients ahead, ~70 min wait
    (15, 100),  # 15 patients ahead, ~100 min wait
    (20, 130),  # 20 patients ahead, ~130 min wait
    (25, 160),  # 25 patients ahead, ~160 min wait
]

# ============================================
# Define what data we expect from the user
# ============================================
class WaitingInput(BaseModel):
    patients_in_queue: int      # How many patients are waiting ahead
    urgency_level: str = "normal"  # Optional: "normal", "urgent", "emergency"


# ============================================
# Average time per patient (in minutes)
# ============================================
# This is a simple assumption: each patient takes about 7 minutes on average
AVERAGE_TIME_PER_PATIENT = 7


def calculate_waiting_time(patients_in_queue):
    """
    Calculate estimated waiting time based on queue length.
    
    Simple formula:
    - Each patient ahead takes about 7 minutes
    - So waiting time = number of patients × 7 minutes
    
    This is a very basic estimation!
    """
    # Multiply patients by average time
    estimated_wait = patients_in_queue * AVERAGE_TIME_PER_PATIENT
    
    return estimated_wait


def adjust_for_urgency(waiting_time, urgency_level):
    """
    Adjust waiting time based on urgency level.
    
    - Emergency: Go to front of queue (minimal wait)
    - Urgent: Wait time reduced by half
    - Normal: Wait the full time
    """
    if urgency_level == "emergency":
        # Emergencies are seen almost immediately
        return 5  # Just 5 minutes for triage
    elif urgency_level == "urgent":
        # Urgent cases wait half the time
        return waiting_time // 2  # Integer division
    else:
        # Normal cases wait the full time
        return waiting_time


def get_waiting_category(minutes):
    """
    Categorize the waiting time into simple categories.
    
    - Under 15 min: Short wait
    - 15-45 min: Moderate wait
    - 45-90 min: Long wait
    - Over 90 min: Very long wait
    """
    if minutes < 15:
        return "SHORT WAIT"
    elif minutes < 45:
        return "MODERATE WAIT"
    elif minutes < 90:
        return "LONG WAIT"
    else:
        return "VERY LONG WAIT"


def format_time(minutes):
    """
    Convert minutes to a nice readable format.
    
    Example: 75 minutes becomes "1 hour 15 minutes"
    """
    if minutes < 60:
        # Less than an hour, just show minutes
        return f"{minutes} minutes"
    else:
        # Calculate hours and remaining minutes
        hours = minutes // 60       # How many full hours
        remaining = minutes % 60    # Remaining minutes
        
        if remaining == 0:
            return f"{hours} hour(s)"
        else:
            return f"{hours} hour(s) and {remaining} minutes"


# ============================================
# API Endpoint - This is what the HTML calls
# ============================================
@app.post("/estimate-wait")
def estimate_waiting_time(data: WaitingInput):
    """
    This function receives queue data and returns wait estimate.
    
    Steps:
    1. Get patients_in_queue and urgency from request
    2. Calculate basic waiting time
    3. Adjust for urgency level
    4. Categorize the wait
    5. Send back the results as JSON
    """
    
    # Step 1: Get the input values
    patients_in_queue = data.patients_in_queue
    urgency_level = data.urgency_level.lower()  # Make lowercase for comparison
    
    # Step 2: Calculate basic waiting time
    basic_wait = calculate_waiting_time(patients_in_queue)
    
    # Step 3: Adjust for urgency level
    adjusted_wait = adjust_for_urgency(basic_wait, urgency_level)
    
    # Step 4: Categorize the wait
    wait_category = get_waiting_category(adjusted_wait)
    
    # Format the time nicely
    formatted_time = format_time(adjusted_wait)
    
    # Step 5: Return the results
    return {
        "estimated_wait_minutes": adjusted_wait,
        "formatted_wait_time": formatted_time,
        "wait_category": wait_category,
        "patients_ahead": patients_in_queue,
        "urgency_level": urgency_level,
        "average_time_per_patient": AVERAGE_TIME_PER_PATIENT,
        "tip": "Bring a book or charger - hospital waits can be long!"
    }


# ============================================
# Health check endpoint (to test if API is running)
# ============================================
@app.get("/")
def home():
    """Simple endpoint to check if the API is working"""
    return {"message": "Waiting Time Estimator API is running!"}
