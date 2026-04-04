import streamlit as st
import pickle

# Load model & scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("💧 Water Footprint Prediction App")

st.write("Enter water usage values to predict footprint")

# User inputs
bathing = st.number_input("Bathing (L)")
cooking = st.number_input("Cooking (L)")
washing = st.number_input("Washing (L)")
gardening = st.number_input("Gardening (L)")
drinking = st.number_input("Drinking (L)")

# Predict
if st.button("Predict"):
    input_data = scaler.transform([[bathing, cooking, washing, gardening, drinking]])
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Water Footprint: {prediction[0]:.2f}")
