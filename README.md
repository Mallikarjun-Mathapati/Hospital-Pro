# ============================================

# AI MINI DASHBOARD - PROJECT README

# ============================================

# This is a simple multi-dashboard project

# that combines 3 student-level mini AI projects.

# ============================================

## 📁 Project Structure

```
hospital 2/
│
├── main.py             ← 🚀 Run this to start ALL servers at once!
├── student_app.py      ← Backend for Student Performance Predictor
├── patient_risk_app.py ← Backend for Patient Risk Checker
├── waiting_time_app.py ← Backend for Waiting Time Estimator
│
├── index.html          ← Main homepage (links to all projects)
├── student.html        ← Frontend for Student Predictor
├── patient.html        ← Frontend for Patient Risk Checker
├── waiting.html        ← Frontend for Waiting Time Estimator
│
├── requirements.txt    ← Python packages needed
└── README.md           ← This file!
```

---

## 🚀 How to Run the Project

### Step 1: Install Python Packages

Open terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

This installs FastAPI and Uvicorn (the server).

---

### Step 2: Start All Servers (EASY WAY - Recommended!)

Just run this ONE command to start all 3 servers at once:

```bash
python main.py
```

You will see:

```
✅ Started: Student Performance Predictor → http://localhost:8001
✅ Started: Patient Risk Checker → http://localhost:8002
✅ Started: Waiting Time Estimator → http://localhost:8003
🎉 ALL SERVERS ARE RUNNING!
```

Press `Ctrl+C` to stop all servers when done.

---

### Step 2 (Alternative): Start Servers Separately

If you prefer to run each server in its own terminal:

**Terminal 1 - Student Performance API (Port 8001):**

```bash
uvicorn student_app:app --reload --port 8001
```

**Terminal 2 - Patient Risk API (Port 8002):**

```bash
uvicorn patient_risk_app:app --reload --port 8002
```

**Terminal 3 - Waiting Time API (Port 8003):**

```bash
uvicorn waiting_time_app:app --reload --port 8003
```

---

### Step 3: Open the Website

1. Open `index.html` in your web browser (just double-click it!)
2. You will see the dashboard with 3 project cards
3. The status dots will turn GREEN when servers are running
4. Click any project card to use it!

---

### ⚠️ Troubleshooting

| Problem                    | Solution                                          |
| -------------------------- | ------------------------------------------------- |
| "Module not found" error   | Run `pip install -r requirements.txt` again       |
| Status dots are RED        | Make sure Python servers are running (Step 2)     |
| "Connection refused" error | Check that all 3 servers started successfully     |
| Port already in use        | Close other programs using ports 8001, 8002, 8003 |

---

## 📌 The 3 Mini Projects Explained

### 1️⃣ Student Performance Predictor

**What it does:**
Predicts a student's exam score based on study hours and attendance.

**How it works (Simple Logic):**

- Each hour of study adds 5 points to the score
- Attendance percentage adds half its value as points
- Formula: `Score = (study_hours × 5) + (attendance × 0.5)`
- Maximum possible score: 100%

**Risk Levels:**

- Below 40% = HIGH RISK (might fail)
- 40-60% = MEDIUM RISK (needs improvement)
- Above 60% = LOW RISK (doing well)

---

### 2️⃣ Hospital Patient Risk Checker

**What it does:**
Checks a patient's health risk level based on age, blood pressure, and blood sugar.

**How it works (Point System):**

- Each factor (age, BP, sugar) gives 0, 1, or 2 risk points
- Total points are added up (max = 6)
- Risk level is determined by total points

**Age Risk:**

- Under 30 = 0 points
- 30-50 = 1 point
- Over 50 = 2 points

**Blood Pressure Risk:**

- Under 120 = 0 points (normal)
- 120-140 = 1 point (elevated)
- Over 140 = 2 points (high)

**Sugar Level Risk:**

- Under 100 = 0 points (normal)
- 100-125 = 1 point (pre-diabetic)
- Over 125 = 2 points (diabetic range)

**Overall Risk:**

- 0-2 points = LOW RISK
- 3-4 points = MEDIUM RISK
- 5-6 points = HIGH RISK

⚠️ **DISCLAIMER:** This is for EDUCATIONAL purposes only!

---

### 3️⃣ Hospital Waiting Time Estimator

**What it does:**
Estimates how long a patient will wait based on queue length and urgency.

**How it works (Simple Calculation):**

- Each patient ahead takes about 7 minutes on average
- Waiting time = Number of patients × 7 minutes
- Urgency level adjusts the wait time:
  - Normal: Wait full time
  - Urgent: Wait half the time
  - Emergency: Only 5 minutes (triage)

**Wait Categories:**

- Under 15 min = SHORT WAIT
- 15-45 min = MODERATE WAIT
- 45-90 min = LONG WAIT
- Over 90 min = VERY LONG WAIT

---

## 🛠️ Technologies Used

- **Python** - Backend programming language
- **FastAPI** - Web framework for creating APIs
- **HTML/CSS** - Frontend web pages
- **JavaScript** - Making pages interactive
- **Uvicorn** - Server to run Python APIs

---

## 📝 Notes for Students

1. All code has comments explaining what each part does
2. The formulas are intentionally simple (not real ML/AI)
3. This project teaches:
   - How frontend (HTML) talks to backend (Python)
   - How to create REST APIs with FastAPI
   - How to use JavaScript fetch() for API calls
   - Basic data processing and decision logic

---

## 🎓 Learning Outcomes

After studying this project, you should understand:

- ✅ How to create a simple API with FastAPI
- ✅ How to connect HTML forms to a Python backend
- ✅ How to display API results on a webpage
- ✅ Basic prediction/calculation logic
- ✅ How to structure a multi-page web project

---
