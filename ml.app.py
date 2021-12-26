import streamlit as st
import numpy as np
import pandas as pd

import joblib

def run_ml_app():
    classifier = joblib.load('loan_data/best_model1.pkl')
    scaler_X = joblib.load('loan_data/scaler_X1.pkl')

    st.subheader('Loan status prediction')
    df = pd.read_csv('loan_data/loan_train2.csv', encoding='ISO-8859-1')

    gender = st.radio('성별을 입력하세요.', ['남자', '여자'])
    if gender == '남자' :
        gender_number = 0
    elif gender == '여자' :
        gender_number = 1   
    print(df.columns)
    married = st.radio('결혼여부를 입력하세요.', ['Married', 'Not Married'])
    if married == 'Not Married' :
        married_number = 0
    elif married == 'Married' :
        married_number = 1
    Dependents = st.sidebar.selectbox('메뉴', menu)










    pregnancies = st.number_input('임신횟수', min_value=0)
    glucose = st.number_input('Glucose', min_value=0)
    pressure = st.number_input('BloodPressure', min_value=0)
    skinthickness = st.number_input('SkinThickness', min_value=0)
    insulin = st.number_input('Insulin', min_value=0)    
    bmi = st.number_input('BMI', min_value=0.0, format='%.1f')
    diabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0, format='%.2f')
    age = st.number_input('AGE',min_value=0)

    if st.button('결과 보기') :
        new_data = np.array([pregnancies,glucose,pressure,
                    skinthickness,insulin,bmi,
                    diabetesPedigreeFunction, age ])

        new_data = new_data.reshape(1, 8)

        new_data = scaler_X.transform(new_data)

        y_pred = classifier.predict(new_data)

        print(y_pred[0])
        if y_pred[0] == 0 :
            st.write('예측 결과는, 당뇨병이 아닙니다.')
        else :
            st.write('예측 결과는, 당뇨병입니다.')


    



