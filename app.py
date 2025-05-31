# Import required libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model
with open("HealthPredictor.pkl", "rb") as f:
    model = pickle.load(f)

# Label decoder function
def decode_label(pred):
    if pred == 0:
        return "Fat"
    elif pred == 1:
        return "Healthy"
    else:
        return "Underweight"

# Set background image directly from URL
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://cdn.pixabay.com/photo/2022/10/09/12/03/athletes-7508975_1280.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# App title and subtitle
st.title("💪 Health Status Predictor")
st.markdown("Predict whether a person is **Underweight**, **Healthy**, or **Fat** based on height and weight using ML.")

# User input
height = st.slider("📏 Height (cm)", 140, 200, 170)
weight = st.slider("⚖️ Weight (kg)", 30, 150, 70)

# Prediction
if st.button("Predict"):
    input_data = pd.DataFrame({'Height_cm': [height], 'Weight_kg': [weight]})
    prediction = model.predict(input_data)
    result = decode_label(prediction[0])

    if result == "Healthy":
        st.markdown("<h3 style='color: green;'>🟢 The person is predicted to be: Healthy</h3>", unsafe_allow_html=True)
    elif result == "Fat":
        st.markdown("<h3 style='color: orange;'>🟠 The person is predicted to be: Fat</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: blue;'>🔵 The person is predicted to be: Underweight</h3>", unsafe_allow_html=True)

# Footer
st.markdown("------------")
st.markdown("<div style='text-align: right;'><h4 style='color: white;'>Developed by: Vishal Pate</h4>", unsafe_allow_html=True)
st.markdown("<div style='text-align: right;'><h4 style='color: white;'>Email: vprakashpate@gmail.com</h4>", unsafe_allow_html=True)
