# 🆔 GOVIND – Aadhaar Region Risk Prediction System

**GOVIND (Geospatial Observation for Vulnerability Identification & National Development)**  
is a Machine Learning based web application designed to predict whether a particular Aadhaar region falls under a **High Risk** or **Low Risk** category based on demographic and temporal indicators.

This system aims to support **UIDAI, government agencies, and disaster management authorities** in identifying vulnerable regions and taking proactive, data-driven decisions.

---

## 🎯 Objective

To analyze region-wise population distribution and time-based trends in order to:
- Detect high-risk Aadhaar regions
- Support disaster preparedness and resource allocation
- Enable early warning and policy planning using AI

---

## 🌟 Key Features

- 📍 Aadhaar region risk classification (High / Low)
- 🧠 XGBoost based ML prediction pipeline
- 📅 Date-wise temporal feature engineering
- 👶 Age-group population vulnerability analysis
- 📈 Growth rate and priority score computation
- 🖥️ Interactive Flask web portal with animated UI

---

## 🧠 Machine Learning Pipeline

The model uses the following engineered features:

### 1. Temporal Features
- Year, Month, Day
- Week number
- Day of week
- Weekend indicator

### 2. Demographic Features
- Population (Age 0–5)
- Population (Age 5–17)
- Population (Age 18+)
- Total population
- Percentage distribution of each age group

### 3. Risk Indicators
- Population growth rate by Pincode
- Priority score based on vulnerable age groups

Model: **XGBoost Classifier (Scikit-Learn Pipeline)**  
Stored using `joblib` and integrated with Flask backend.

---

## 🖥️ Technology Stack

| Layer        | Technology |
|---------------|------------|
| Frontend      | HTML, CSS (Animated, Responsive UI) |
| Backend       | Flask (Python) |
| Data Handling | Pandas, NumPy |
| ML Model      | XGBoost, Scikit-learn |
| Model Storage | Joblib |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
GOVIND-ML-Portal/
|
|-- flask_app.py                # Flask backend application
|-- requirements.txt           # Project dependencies
|-- aadhaar_risk_pipeline.pkl  # Trained XGBoost ML pipeline (ignored in Git)
|-- .gitignore                 # Git ignore rules (venv, model, cache, etc.)
|
|-- templates/                 # HTML templates
|   |-- index.html             # Home page
|   |-- prediction.html        # Risk prediction page
|
|-- static/                    # Static assets (CSS, images)
|   |-- style1.css             # Home page styling
|   |-- prediction.css        # Prediction page styling
|
`-- README.md                  # Project documentation
```

---

## ▶️ How to Run the Project

```bash
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python flask_app.py
