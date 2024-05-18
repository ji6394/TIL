import streamlit as st
import numpy as np
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.preprocessing import OneHotEncoder

# 모델 로드
model =TabularPredictor.load('C:/Users/82108/sds/bears/AutogluonModels/ag-20240312_090653')

# 원본 데이터프레임에서 필요한 컬럼 추출
original_df = pd.read_csv("C:/Users/82108/sds/bears/original_df.csv")
selected_features = ['week', 'home', 'away', 'weather', 'temp', '강수량(mm)', '연', '월', '일', 'holiday']

import streamlit as st

form = st.form(key="my_form")
for feature in selected_features:
    input_value = form.text_input(label=feature, key=feature)
submitted = form.form_submit_button()  # Update to use form_submit_button for submit




# 사용자 입력값으로 새로운 데이터프레임 생성
if submitted:
    user_input = {key: value for key, value in form.inputs.items()}
    new_df = original_df[selected_features].copy()
    for key, value in user_input.items():
        new_df[key] = value

    # 전처리 코드 적용 (원본 코드에서 필요한 부분만 추출하여 사용)
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
    new_df.drop(['week'], axis=1, inplace=True)

    encoder = OneHotEncoder(sparse=False)
    home_encoded = encoder.fit_transform(new_df['home'].values.reshape(-1, 1))
    away_encoded = encoder.fit_transform(new_df['away'].values.reshape(-1, 1))
    new_df[['home' + str(i) for i in range(home_encoded.shape[1])]] = home_encoded
    new_df[['away_' + str(i) for i in range(away_encoded.shape[1])]] = away_encoded
    new_df.drop(['home','away'], axis=1, inplace=True)
    
    desired_categories_order = {'맑음':0, '구름조금':1, '구름많음':2, '흐림':3, '비':4}
    new_df['weather_encoded'] = new_df['weather'].map(desired_categories_order)
    new_df.drop(['weather'], axis=1, inplace=True)

    new_df.drop(['day_num'],axis=1, inplace=True)

    # 예측 수행
    prediction = model.predict(new_df)

    # 결과 출력
    st.write("예측 spec 값:", prediction)