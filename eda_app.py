import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app() :
    st.subheader('Exploratory Data Analysis')
    
    df = pd.read_csv('loan_data/loan_train2.csv', encoding='ISO-8859-1')

    st.dataframe( df )

    st.subheader('Nan 데이터 확인')

    st.dataframe( df.isna().sum())

    st.subheader('각 컬럼별 히스토그램 확인')

    selected_column = st.selectbox('컬럼을 선택하세요', df.columns)

    bins = st.slider('bin의 갯수 조절', min_value=10, max_value=50)

    fig1 = plt.figure()
    df[selected_column].hist(bins= bins)
    st.pyplot(fig1)

    st.subheader('각 컬럼별 통계치')
    st.dataframe(df.describe())

    radio_menu = ['데이터프레임', '통계치' ]
    selected_radio = st.radio('선택하세요', radio_menu)

    if selected_radio == '데이터프레임' :
        st.dataframe(df)
    elif selected_radio == '통계치' :
        st.dataframe( df.describe() )
    
    # 컬럼을 선택하면, 해당 컬럼들만 데이터프레임 표시하는 화면
    print(df.columns)

    selected_columns = st.multiselect('컬럼을 선택하세요', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe( df[selected_columns] )
    else :
        st.write('선택한 컬럼이 없습니다.')

    # 상관관계 분석을 위한, 상관계수 보여주는 화면 개발

    st.subheader('상관계수')
    # st.dataframe( df.corr() )

    df_corr = df.iloc[ : , 3 :  ]
    
    selected_corr = st.multiselect('상관계수 컬럼 선택', df_corr.columns)

    # 유저가 1개라도 컬럼을 선택했을 경우
    if len(selected_corr) > 0 :
        st.dataframe( df_corr[selected_corr].corr() )

        # 상관계수를 수치로도 구하고, 차트로도 표시하라.
        
        fig1 = sns.pairplot(data=  df_corr[selected_corr] )
        st.pyplot(fig1)
    # 유저가 컬럼을 선택하지 않은 경우
    else :
        st.write('선택한 컬럼이 없습니다.')


    # 유저가 컬럼을 선택하면, 
    # 해당 컬럼의 min과 max에 해당하는 사람이 누구인지
    # 그 사람의 데이터를 화면에 보여주는 기능 개발

    ### 문자열 데이터가 아닌, 컬럼들만 가져오는 코드!!! ###
