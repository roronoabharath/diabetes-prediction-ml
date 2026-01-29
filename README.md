# 🩺 Diabetes Prediction Web App

## 📌 Project Overview
This project is an interactive web application built using **Streamlit** that predicts whether a person is likely to have diabetes based on health-related inputs.  
It uses a machine learning classification model trained on a healthcare dataset.

---

## 📁 Project Structure

- `app.py` – Streamlit-based web application
- `train_model.py` – Script used to train and save the ML model
- `diabetes_prediction_model.pkl` – Trained machine learning model
- `diabetes_prediction_dataset.csv` – Dataset used for training
- `base.ipynb` – Initial experimentation and exploration notebook

---

## ⚙️ Features

- Simple and intuitive user interface
- Input fields:
  - Age
  - Hypertension (Yes/No)
  - Heart Disease (Yes/No)
  - BMI
  - HbA1c Level
  - Blood Glucose Level
  - Gender
  - Smoking History
- Real-time prediction output:
  - ✅ **Positive**
  - ❌ **Negative**

---

## 🧠 Model Details

- Task: Binary classification (Diabetes: Yes / No)
- Algorithm: Logistic Regression
- Preprocessing steps:
  - Categorical features encoded numerically
  - Missing values handled using mean imputation
  - Feature consistency maintained between training and inference
- Total features used: **8**

---

## ▶️ How to Run the App

### Install required packages
```bash
pip install streamlit pandas scikit-learn
