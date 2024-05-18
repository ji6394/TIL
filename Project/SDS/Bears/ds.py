import streamlit as st
import numpy as np
import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.preprocessing import OneHotEncoder

# 모델 로드
model = TabularPredictor.load('C:/Users/82108/sds/bears/AutogluonModels/ag-20240312_090653')

# 원본 데이터프레임에서 필요한 컬럼 추출
original_df = pd.read_csv("C:/Users/82108/sds/bears/original_df.csv")
selected_features = ['week', 'home', 'away', 'weather', 'temp', '강수량(mm)', '연', '월', '일', 'holiday']

# 추가된 코드: 원하는 순서로 범주를 나열
desired_categories_order = {'맑음':0, '구름조금':1, '구름많음':2, '흐림':3, '비':4}

# 초기화된 세션 상태 속성
if 'form' not in st.session_state:
    st.session_state.form = {feature: "" for feature in selected_features}

form = st.form(key="my_form")
for feature in selected_features:
    input_value = form.text_input(label=feature, key=feature, value=st.session_state.form[feature])
    st.session_state.form[feature] = input_value
submitted = form.form_submit_button("Submit")

if submitted:
    user_input = st.session_state.form  # Get the data from the submitted form 
    new_row = {}  # Create an empty dictionary to store user input for the new row
    for key, value in user_input.items():
        new_row[key] = value
    new_df = pd.DataFrame([new_row])  # Create a new dataframe with a single row containing user input

    # 전처
    day_name_num = {
        '월': 1,
        '화': 2,
        '수': 3,
        '목': 4,
        '금': 5,
        '토': 6,
        '일': 7
        }
    new_df['day_num'] = new_df['week'].map(day_name_num)
    new_df['day_sin'] = np.sin(2 * np.pi * new_df['day_num']/7.0)
    new_df['day_cos'] = np.cos(2 * np.pi * new_df['day_num']/7.0)
    new_df.drop(['week', 'day_num'], axis=1, inplace=True)

    # OneHotEncoder 초기화 및 학습 데이터에 맞춤
    encoder = OneHotEncoder(sparse=False)
    encoder.fit(original_df['home'].values.reshape(-1, 1))
    home_encoded = encoder.transform(new_df['home'].values.reshape(-1, 1))
    encoder.fit(original_df['away'].values.reshape(-1, 1))
    away_encoded = encoder.transform(new_df['away'].values.reshape(-1, 1))

    # home_encoded와 away_encoded로부터 DataFrame 생성
    home_df = pd.DataFrame(home_encoded, columns=[f'home{i}' for i in range(home_encoded.shape[1])])
    away_df = pd.DataFrame(away_encoded, columns=[f'away_{i}' for i in range(away_encoded.shape[1])])

    # home_df와 away_df를 병합하여 new_df 생성
    new_df = pd.concat([new_df, home_df, away_df], axis=1)

    new_df.drop(['home', 'away'], axis=1, inplace=True)

    new_df['weather_encoded'] = new_df['weather'].map(desired_categories_order)
    new_df.drop(['weather'], axis=1, inplace=True)

    # 예측 수행
    prediction = model.predict(new_df)

    # 결과 출력
    st.write("예측 spec 값:", prediction)
