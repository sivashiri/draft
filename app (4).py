import streamlit as st
import pickle
import numpy as np
import streamlit as st
import sklearn


# Load trained model
with open('payzone_mlp_model.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("🏞️ Payzone Prediction App")
st.write("Enter reservoir properties to predict if it's a potential **oil/gas payzone**.")

# Input fields
porosity = st.number_input("Porosity (percentage, e.g. 15)", min_value=0.0, max_value=100.0, step=0.01)
water_saturation = st.number_input("Water Saturation (percentage, e.g. 25)", min_value=0.0, max_value=100.0, step=0.01)
permeability = st.number_input("Permeability (mD)", min_value=0.0, step=1.0)
net_pay_thickness = st.number_input("Net Pay Thickness (m)", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    # Prepare input
    input_data = np.array([[porosity, water_saturation, permeability, net_pay_thickness]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == 1:
        st.success("✅ This zone is likely a **Payzone**.")
    else:
        st.warning("⚠️ This zone is likely **Not a Payzone**.")
