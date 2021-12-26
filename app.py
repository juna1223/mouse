import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    menu = ['Home', 'EDA', 'Prediction']

    choice = st.sidebar.selectbox('menu choice', menu)

    if choice == 'Home' :
        st.subheader('대출 가능 여부 예측')

    elif choice == 'EDA' :
        run_eda_app()

    elif choice == 'Prediction' :
        run_ml_app()

if __name__ == '__main__' :
    main()

