# 💧 Groundwater Quality Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether groundwater is **safe or unsafe** based on chemical parameters such as pH, nitrate (NO3), chloride (Cl), sulfate (SO4), and others.

---

## ⚙️ Workflow

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training (Logistic, Random Forest, XGBoost, etc.)
5. Model Comparison
6. Final Ensemble Model (Voting Classifier)
7. Deployment using Streamlit

---

## 🤖 Models Used

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* KNN
* XGBoost
* Voting Classifier (Final Model)

---

## 📊 Results

* Achieved high accuracy using ensemble learning
* Identified key parameters affecting water quality
* Strong ROC-AUC performance

---

## 🌐 Streamlit Demo

This project includes a Streamlit app for real-time prediction.

⚠️ Note:
The app uses simplified inputs. The original model was trained on a larger feature set, so predictions in the demo may not always be fully accurate.

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

* app.py → Streamlit UI
* results/models → trained models
* results/plots → visualizations
* dataset → groundwater data

---

## 👨‍💻 Author

Tushar Kacha,
Kishor Goraniya,
Vishal Amethiya
