import streamlit as st
import numpy as np
import pickle

# Load model
with open("diabetes_prediction_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

st.title("Diabetes Prediction App")

# Inputs
age = st.number_input("Age", 0, 120, 30)
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
bmi = st.number_input("BMI", 0.0, 100.0, 25.0)
HbA1c_level = st.number_input("HbA1c Level", 0.0, 20.0, 5.5)
blood_glucose_level = st.number_input("Blood Glucose Level", 0, 600, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
smoking_history = st.selectbox(
    "Smoking History",
    ["never", "former", "current", "not current", "ever"]
)

# Encoding (MUST match training)
gender_encoded = 0 if gender == "Male" else 1

smoking_mapping = {
    "never": 0,
    "former": 1,
    "current": 2,
    "not current": 3,
    "ever": 4
}
smoking_encoded = smoking_mapping[smoking_history]

user_input = np.array([[
    age,
    1 if hypertension == "Yes" else 0,
    1 if heart_disease == "Yes" else 0,
    bmi,
    HbA1c_level,
    blood_glucose_level,
    gender_encoded,
    smoking_encoded
]])

# Prediction
if st.button("Predict Diabetes"):
    prediction = loaded_model.predict(user_input)
    result = "Positive" if prediction[0] == 1 else "Negative"
    st.success(f"Predicted Diabetes Outcome: {result}")
