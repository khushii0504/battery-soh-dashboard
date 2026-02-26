import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Battery SOH Dashboard",
    page_icon="🔋",
    layout="wide"
)

st.title("🔋 Battery State of Health (SOH) Prediction")
st.markdown("Random Forest based Battery SOH Estimation")

# -----------------------------------
# Load Model
# -----------------------------------
@st.cache_resource
def load_model():
    if os.path.exists("rf_model.pkl"):
        return joblib.load("rf_model.pkl")
    return None

model = load_model()

if model is None:
    st.error("Model file 'rf_model.pkl' not found.")
    st.stop()

st.success("Model loaded successfully!")

st.markdown("---")

# -----------------------------------
# Input Section
# -----------------------------------
st.header("Enter Battery Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    cycle = st.number_input("Cycle Number", min_value=1, max_value=1000, value=50)

with col2:
    rolling_mean = st.number_input("Rolling Mean Capacity", value=1.9)

with col3:
    rolling_std = st.number_input("Rolling Std Capacity", value=0.01)

st.markdown("")

if st.button("Predict SOH"):

    input_data = np.array([[cycle, rolling_mean, rolling_std]])
    prediction = model.predict(input_data)

    st.success(f"Predicted SOH: {prediction[0]:.4f}")

st.markdown("---")

# -----------------------------------
# Visualization
# -----------------------------------
st.header("Simulated SOH Degradation Trend")

cycles = np.arange(1, 101)
simulated_soh = 1 - 0.0005 * cycles

chart_data = pd.DataFrame({
    "Cycle": cycles,
    "SOH": simulated_soh
}).set_index("Cycle")

st.line_chart(chart_data)