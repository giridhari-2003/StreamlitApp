import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('heart_deasease.pkl', 'rb') as file:
    # model = pickle.load(file)
    data = pickle.load(file)
    model = data['model']

# Title
st.title("Heart Disease Prediction")

# Input fields for the features
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=50)
with col2:
    sex = st.selectbox("Sex", options=[0, 1])  # 0: Female, 1: Male
with col3:
    exang = st.selectbox("Exercise Induced Angina \n(exang)", options=[0, 1])  # 0: No, 1: Yes
    # cp = st.number_input("Chest Pain Type (cp)", min_value=0, max_value=3, value=1)

# Second row of inputs
col4, col5, col6 = st.columns(3)
with col4:
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
with col5:
    chol = st.number_input("Serum Cholestoral in mg/dl (chol)", min_value=100, max_value=600, value=200)
with col6:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])  # 0: False, 1: True

# Third row of inputs
col7, col8, col9 = st.columns(3)
with col7:
    restecg = st.number_input("Resting Electrocardiographic Results (restecg)", min_value=0, max_value=2, value=1)
with col8:
    thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=60, max_value=220, value=150)
with col9:
    cp = st.number_input("Chest Pain Type (cp)", min_value=0, max_value=3, value=1)
    # exang = st.selectbox("Exercise Induced Angina \n(exang)", options=[0, 1])  # 0: No, 1: Yes
    # st.markdown("**Exercise Induced Angina**<br>(exang)", unsafe_allow_html=True)
    # exang = st.selectbox("", options=[0, 1])  # 0: No, 1: Yes

# Fourth row of inputs
col10, col11, col12 = st.columns(3)
with col10:
    oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=10.0, value=1.0)
with col11:
    slope = st.number_input("Slope of the Peak Exercise ST Segment (slope)", min_value=0, max_value=2, value=1)
with col12:
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (ca)", min_value=0, max_value=4, value=0)

# age = st.number_input("Age", min_value=0, max_value=120, value=50)
# sex = st.selectbox("Sex", options=[0, 1])  # 0: Female, 1: Male
# cp = st.number_input("Chest Pain Type (cp)", min_value=0, max_value=3, value=1)
# trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
# chol = st.number_input("Serum Cholestoral in mg/dl (chol)", min_value=100, max_value=600, value=200)
# fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])  # 0: False, 1: True
# restecg = st.number_input("Resting Electrocardiographic Results (restecg)", min_value=0, max_value=2, value=1)
# thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=60, max_value=220, value=150)
# exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1])  # 0: No, 1: Yes
# oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=10.0, value=1.0)
# slope = st.number_input("Slope of the Peak Exercise ST Segment (slope)", min_value=0, max_value=2, value=1)
# ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (ca)", min_value=0, max_value=4, value=0)
thal = st.number_input("Thalassemia (thal)", min_value=0, max_value=3, value=2)

# Prepare the data for prediction
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.markdown("<h2><strong>The model predicts that the patient has heart disease.</strong></h2>",
                    unsafe_allow_html=True)
    else:
        st.markdown("<h2><strong>The model predicts that the patient does not have heart disease.</strong></h2>",
                    unsafe_allow_html=True)
    # if prediction[0] == 1:
    #     st.markdown("The model predicts that the patient **has** heart disease.")
    # else:
    #     st.markdown("The model predicts that the patient **does not have** heart disease.")
