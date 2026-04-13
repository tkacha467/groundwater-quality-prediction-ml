import streamlit as st
import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "results", "models", "soft_voting_final.pkl")
scaler_path = os.path.join(BASE_DIR, "results", "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

st.title("💧 Groundwater Quality Prediction")

st.write("Demo prediction using key chemical parameters")

# Inputs
ph = st.number_input("pH", value=7.5)
no3 = st.number_input("NO3", value=10.0)
cl = st.number_input("Cl", value=50.0)
so4 = st.number_input("SO4", value=30.0)
th = st.number_input("TH", value=200.0)
na = st.number_input("Na", value=50.0)

if st.button("Predict"):

    # ⚠️ IMPORTANT: match model feature size (dummy values added)
    data = np.ones((1, 25)) * 50

    # fill important inputs
    data[0][0] = ph      # pH
    data[0][5] = no3     # NO3
    data[0][3] = cl      # Cl
    data[0][4] = so4     # SO4
    data[0][6] = th      # TH
    data[0][9] = na      # Na   

    data_scaled = scaler.transform(data)
    result = model.predict(data_scaled)

    if result[0] == 0:
        st.success("✅ Water is SAFE")
    else:
        st.error("❌ Water is UNSAFE")

st.subheader("📊 Model Performance")

st.image("results/plots/07_model_comparison.png", caption="Model Accuracy Comparison")

st.subheader("📉 Confusion Matrix & ROC Curve")

st.image("results/plots/08_confusion_roc.png", caption="Confusion Matrix & ROC")

st.subheader("🔥 Feature Correlation")

st.image("results/plots/03_correlation_heatmap.png", caption="Correlation Heatmap")