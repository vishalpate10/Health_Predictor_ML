import streamlit as st
import pandas as pd
import pickle

# Load the model
with open("HealthPredictor.pkl", "rb") as f:
    model = pickle.load(f)

def decode_label(pred):
    if pred == 0:
        return "Fat"
    elif pred == 1:
        return "Healthy"
    else:
        return "Underweight"

# Inject background CSS (no f-string, no indentation inside string)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://cdn.pixabay.com/photo/2022/10/09/12/03/athletes-7508975_1280.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💪 Health Status Predictor")
st.markdown("Predict whether a person is **Underweight**, **Healthy**, or **Fat** based on height and weight using ML.")

height = st.slider("📏 Height (cm)", 140, 200, 170)
weight = st.slider("⚖️ Weight (kg)", 30, 150, 70)

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

st.markdown("------------")
st.markdown("<div style='text-align: right;'><h4 style='color: white;'>Developed by: Vishal Pate</h4></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: right;'><h4 style='color: white;'>Email: vprakashpate@gmail.com</h4></div>", unsafe_allow_html=True)
