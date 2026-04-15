"""
Created on Wed Oct 15 13:10:34 2025
@author: Thejeswar Reddy
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# ----------------------------------------------------------
# Load Trained Models
# ----------------------------------------------------------
working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(r"C:\Users\vamsi\OneDrive\Documents\csp-project\diabetes_model (2).sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\vamsi\OneDrive\Documents\csp-project\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\vamsi\OneDrive\Documents\csp-project\parkinsons_model.sav", 'rb'))

# ----------------------------------------------------------
# Sidebar Navigation
# ----------------------------------------------------------
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinsons Prediction"],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# ----------------------------------------------------------
# 1️⃣ Diabetes Prediction Page
# ----------------------------------------------------------
if selected == 'Diabetes Prediction':
    st.title('🩸 Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0)
    with col3:
        BMI = st.number_input('BMI value', min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0)
    with col2:
        Age = st.number_input('Age of the Person', min_value=1)

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# ----------------------------------------------------------
# 2️⃣ Heart Disease Prediction Page
# ----------------------------------------------------------
if selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1)
    with col2:
        sex = st.selectbox('Sex (0 = Female, 1 = Male)', [0, 1])
    with col3:
        cp = st.number_input('Chest Pain type (0–3)', min_value=0, max_value=3)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
    with col2:
        chol = st.number_input('Serum Cholesterol in mg/dl', min_value=0.0)
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0–2)', min_value=0, max_value=2)
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0.0)
    with col3:
        exang = st.selectbox('Exercise Induced Angina', [0, 1])
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0)
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (0–2)', min_value=0, max_value=2)
    with col3:
        ca = st.number_input('Major vessels colored by fluoroscopy (0–3)', min_value=0, max_value=3)
    with col1:
        thal = st.number_input('Thal (0=normal, 1=fixed defect, 2=reversible defect)', min_value=0, max_value=2)

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                      exang, oldpeak, slope, ca, thal]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# ----------------------------------------------------------
# 3️⃣ Parkinson's Disease Prediction Page
# ----------------------------------------------------------
if selected == "Parkinsons Prediction":
    st.title("🧠 Parkinson's Disease Prediction using ML")

    labels = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]

    cols = st.columns(5)
    inputs = []

    for i, label in enumerate(labels):
        with cols[i % 5]:
            inputs.append(st.number_input(label, value=0.0))

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        user_input = [float(x) for x in inputs]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
