import streamlit as st
import numpy as np
import pandas as pd

import joblib

def run_ml_app():
    classifier = joblib.load('loan_data/best_model1.pkl')
    scaler_X = joblib.load('loan_data/scaler_X1.pkl')

    st.title('Loan status prediction')
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
    
    Dependents = st.selectbox('부양가족 수(3인 이상 일 시, 3+으로 체크)',pd.Series(['0','1','2','3+']))
    if Dependents == '0' :
        Dependents_number = 0
    elif Dependents == '1' :
        Dependents_number = 1
    elif Dependents == '2' :
        Dependents_number = 2
    elif Dependents == '3+' :
        Dependents_number = 3
    
    Education = st.radio('대학 졸업 여부를 입력하세요.', ['대학 졸업', '대학 미졸업'])
    if Education == '대학 미졸업' :
        Education_number = 0
    elif Education == '대학 졸업' :
        Education_number = 1
    
    Self_Employed = st.radio('자영업을 하고 계신가요?', ['O', 'X'])
    if Self_Employed == 'X' :
        Self_Employed_number = 0
    elif Self_Employed == 'O' :
        Self_Employed_number = 1
    
    ApplicantIncome = st.number_input('신청인 소득 입력', min_value=df['ApplicantIncome'].min(), max_value=df['ApplicantIncome'].max())
    
    CoapplicantIncome = st.number_input('공동 신청인 소득 입력(공동 신청인이 없을 시 0 기입)', min_value=df['CoapplicantIncome'].min(), max_value=df['CoapplicantIncome'].max())
    
    LoanAmount = st.number_input('대출 금액', min_value=df['LoanAmount'].min(), max_value=df['LoanAmount'].max())
    
    Credit_History = st.radio('신용 이력에 결격 사유가 있나요?', ['O', 'X'])
    if  Credit_History == 'O' :
        Credit_History_number = 0
    elif Credit_History == 'X' :
        Credit_History_number = 1
    
    Property_Area = st.selectbox('거주지(Property_area)',pd.Series(['시골(rural)','준도시(semiurban)','도시(urban)']))
    if Property_Area == '시골(rural)' :
        Property_Area_number = 0
    elif Property_Area == '준도시(semiurban)' :
        Property_Area_number = 1
    elif Property_Area == '도시(urban)' :
        Property_Area_number = 2


    if st.button('결과 보기') :
        new_data = np.array([gender_number,married_number,Dependents_number,
                    Education_number,Self_Employed_number,ApplicantIncome,
                    CoapplicantIncome, LoanAmount,Credit_History_number,
                    Property_Area_number])

        new_data = new_data.reshape(1, 10)

        new_data = scaler_X.transform(new_data)

        y_pred = classifier.predict(new_data)

        print(y_pred[0])
        if y_pred[0] == 0 :
            st.write('예측 결과는, 대출이 불가능 합니다.')
        else :
            st.write('예측 결과는, 대출이 가능 합니다.')


    



