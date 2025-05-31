# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the saved model
with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load label encoder
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# Set background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://cdn.pixabay.com/photo/2020/06/01/17/28/health-5248011_1280.jpg');
        background-size: cover;
        background-position: center;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("💪 Health Status Predictor")
st.markdown("Predict whether a person is **Underweight**, **Healthy**, or **Fat** based on height and weight.")

# User inputs
height = st.slider("📏 Height (cm)", 140, 200, 170)
weight = st.slider("⚖️ Weight (kg)", 30, 150, 70)

# Prediction button
if st.button("Predict"):
    input_data = pd.DataFrame({'Height_cm': [height], 'Weight_kg': [weight]})
    prediction = model.predict(input_data)
    result = le.inverse_transform(prediction)[0]

    if result == "Healthy":
        st.markdown("<h3 style='color: green;'>🟢 The person is predicted to be: Healthy</h3>", unsafe_allow_html=True)
    elif result == "Fat":
        st.markdown("<h3 style='color: orange;'>🟠 The person is predicted to be: Fat</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: blue;'>🔵 The person is predicted to be: Underweight</h3>", unsafe_allow_html=True)

# Horizontal line
st.markdown("------------")

# Developer credit
st.markdown("<div style='text-align: right;'><h4 style='color: white;'>Developed by: Vishal Pate</h4>", unsafe_allow_html=True) 
st.markdown("<div style='text-align: right;'><h4 style='color: white;'>Email: vprakashpate@gmail.com</h4>", unsafe_allow_html=True)
