# 💧 Groundwater Quality Prediction using Machine Learning

## 📌 Overview

This project predicts whether groundwater is safe or unsafe based on chemical parameters like pH, nitrate, chloride, etc.

## ⚙️ Features

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Multiple ML models (Logistic Regression, Random Forest, XGBoost, etc.)
* Model comparison using accuracy and ROC-AUC
* Final ensemble model (Voting Classifier)
* Streamlit web app for prediction

## 📊 Results

* Achieved high accuracy using ensemble methods
* Identified key chemical factors affecting water quality

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ⚠️ Note

The Streamlit app is a simplified demo. Full prediction requires all input features used during training.

## 📁 Project Structure

* app.py → Streamlit UI
* results/models → saved models (.pkl)
* results/plots → visualizations
* dataset → groundwater data

## 👨‍💻 Author

Tushar Kacha,
Kishor Goraniya,
Vishal Amethiya
