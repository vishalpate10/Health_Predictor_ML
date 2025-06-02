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

# Background image without color property
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.byoprotein.com/wp-content/uploads/2018/01/fitness-man-desktop-wallpaper-51316-53014-hd-wallpapers.jpg');
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💪 BMI (Body Mass Index) Status")
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
