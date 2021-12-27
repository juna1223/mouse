import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from PIL import Image
from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    menu = ['Home', 'EDA', 'Prediction']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home' :
        st.title('Loan status Prediction')
        image = Image.open('loan_data/loan_hand.jpg')
        st.image(image)
        st.subheader('대출이 가능할 지 예측해보는 앱')

    elif choice == 'EDA' :
        run_eda_app()

    elif choice == 'Prediction' :
        run_ml_app()

if __name__ == '__main__' :
    main()

