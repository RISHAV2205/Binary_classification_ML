import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("liver_model.pkl")
scaler = joblib.load("scaler.pkl")

# App title
st.title("🩺 Liver Disease Prediction System")
st.write("Enter patient details to predict liver disease")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=45)

gender = st.selectbox("Gender", ("Male", "Female"))
gender = 1 if gender == "Male" else 0

total_bilirubin = st.number_input("Total Bilirubin", value=1.2)
direct_bilirubin = st.number_input("Direct Bilirubin", value=0.5)
alkaline_phosphotase = st.number_input("Alkaline Phosphotase", value=210)
alamine_aminotransferase = st.number_input("ALT", value=35)
aspartate_aminotransferase = st.number_input("AST", value=40)
total_proteins = st.number_input("Total Proteins", value=6.8)
albumin = st.number_input("Albumin", value=3.2)
ag_ratio = st.number_input("Albumin and Globulin Ratio", value=0.9)

# Predict button
if st.button("Predict"):
    input_data = np.array([[
        age, gender, total_bilirubin, direct_bilirubin,
        alkaline_phosphotase, alamine_aminotransferase,
        aspartate_aminotransferase, total_proteins,
        albumin, ag_ratio
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Liver Disease Detected")
    else:
        st.success("✅ No Liver Disease Detected")
