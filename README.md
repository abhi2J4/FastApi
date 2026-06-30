# 🏥 Insurance Premium Category Prediction using FastAPI & Streamlit

A Machine Learning-powered web application that predicts an individual's **Insurance Premium Category** based on their health, lifestyle, occupation, and income details. The project uses a trained Scikit-learn model served through **FastAPI** with an interactive **Streamlit** frontend.

---

## 📌 Project Overview

This project demonstrates how to deploy a Machine Learning model using **FastAPI** as the backend API and **Streamlit** as the frontend user interface.

The application accepts user information such as:

- Age
- Height
- Weight
- Annual Income
- Smoking Status
- City
- Occupation

It automatically performs feature engineering (BMI, Age Group, Lifestyle Risk, City Tier) before sending the processed data to the trained ML model for prediction.

---

## 🚀 Features

- ✅ Interactive Streamlit UI
- ✅ FastAPI REST API
- ✅ Automatic Feature Engineering
- ✅ BMI Calculation
- ✅ Lifestyle Risk Detection
- ✅ Age Group Classification
- ✅ City Tier Classification
- ✅ Pre-trained Machine Learning Model (.pkl)
- ✅ JSON API Response
- ✅ Pydantic Input Validation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | Backend API |
| Streamlit | Frontend |
| Scikit-Learn | Machine Learning Model |
| Pandas | Data Processing |
| Pydantic | Request Validation |
| Uvicorn | ASGI Server |
| Pickle | Model Serialization |

---

## 📂 Project Structure

```
FastApi/
│
├── app.py              # Insurance Premium Prediction API
├── frontend.py         # Streamlit Web Application
├── model.pkl           # Trained ML Model
├── requirements.txt
├── patients.json
├── main.py             # Patient Management FastAPI APIs
├── test.py
└── README.md
```

---

## ⚙️ How It Works

### Step 1

The user enters:

- Age
- Weight
- Height
- Income
- Smoker Status
- City
- Occupation

↓

### Step 2

FastAPI computes additional features:

- BMI
- Lifestyle Risk
- Age Group
- City Tier

↓

### Step 3

The processed features are converted into a Pandas DataFrame.

↓

### Step 4

The trained ML model predicts the insurance premium category.

↓

### Step 5

The prediction is returned as JSON and displayed in the Streamlit application.

---

## 🧮 Feature Engineering

The API automatically creates additional features before prediction.

### BMI

```
BMI = Weight / Height²
```

### Lifestyle Risk

| Condition | Risk |
|------------|------|
| Smoker + BMI > 30 | High |
| Smoker + BMI > 27 | Medium |
| Otherwise | Low |

### Age Groups

| Age | Group |
|------|-------|
| <25 | Young |
| 25–44 | Adult |
| 45–59 | Middle Aged |
| ≥60 | Senior |

### City Tier

| Tier | Cities |
|------|--------|
| Tier 1 | Mumbai, Delhi, Bangalore, Chennai, Hyderabad, Pune, Kolkata |
| Tier 2 | Major developing cities |
| Tier 3 | Remaining cities |

---

## 🖥️ API Endpoint

### POST `/predict`

Predicts the insurance premium category.

### Request Body

```json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 12,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

### Response

```json
{
    "predicted_category": "Medium"
}
```

---

## ▶️ Running the Project

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/FastApi.git

cd FastApi
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Start FastAPI Server

```bash
uvicorn app:app --reload
```

API will run at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

### 4. Run Streamlit

```bash
streamlit run frontend.py
```

The application opens automatically in your browser.

---

## 📸 Application Preview

### Streamlit Frontend

*(Add screenshot here)*

Example:

```
Insurance Premium Category Predictor

Age
Weight
Height
Income
Smoker
City
Occupation

[ Predict ]
```

---

## 📦 Dependencies

Main packages used:

- FastAPI
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Pydantic
- Uvicorn
- Joblib

Install using:

```bash
pip install -r requirements.txt
```

---

## 🔒 Input Validation

Pydantic validates:

- Age between 1 and 119
- Height > 0 and < 2.5 m
- Weight > 0
- Income > 0
- Occupation from predefined values

Invalid requests return appropriate HTTP error responses.

---

## 📚 Additional FastAPI Module

The repository also contains a **Patient Management System API** that demonstrates CRUD operations using FastAPI.

Features include:

- Create Patient
- View Patient
- Update Patient
- Sort Patients
- Automatic BMI Calculation
- BMI Verdict
- JSON Database Storage

---

## 📈 Future Improvements

- Docker Support
- Database Integration (MySQL/PostgreSQL)
- User Authentication
- Cloud Deployment (Render/AWS/Azure)
- Model Retraining Pipeline
- Logging and Monitoring
- CI/CD Pipeline

---

## 👨‍💻 Author

**Abhi2J4**

GitHub: https://github.com/abhi2J4

---

## ⭐ If you found this project useful

Give this repository a ⭐ on GitHub and feel free to contribute!
