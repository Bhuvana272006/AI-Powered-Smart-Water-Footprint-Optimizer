import streamlit as st
import pickle
def recommend(max_activity):
    if max_activity == "Bathing(L)":
        return "Reduce shower time or use low-flow showerheads."
    elif max_activity == "Cooking(L)":
        return "Use water-efficient cooking methods."
    elif max_activity == "Washing(L)":
        return "Run washing machine with full loads only."
    elif max_activity == "Gardening(L)":
        return "Adopt drip irrigation / reuse household water for gardening."
    elif max_activity == "Drinking(L)":
        return "Check for leaks / encourage mindful drinking."
    else:
        return "Maintain current usage."
# Load model & scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
import os

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))
st.title("💧 Water Footprint Prediction App")

st.write("Enter water usage values to predict footprint")

# User inputs
bathing = st.number_input("Bathing (L)")
cooking = st.number_input("Cooking (L)")
washing = st.number_input("Washing (L)")
gardening = st.number_input("Gardening (L)")
drinking = st.number_input("Drinking (L)")
activities = {
    "Bathing(L)": bathing,
    "Cooking(L)": cooking,
    "Washing(L)": washing,
    "Gardening(L)": gardening,
    "Drinking(L)": drinking
}

max_activity = max(activities, key=activities.get)
# Predict
if st.button("Predict"):
    total_usage = bathing + cooking + washing + gardening + drinking
    input_data = scaler.transform([[bathing, cooking, washing, gardening, drinking, total_usage]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Water Footprint: {prediction[0]:.2f}")
suggestion = recommend(max_activity)

st.info(f"💡 Recommendation: {suggestion}")
