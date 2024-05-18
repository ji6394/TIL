import streamlit as st
import numpy as np
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor

# 모델 로드
model = TabularPredictor.load('C:/Users/82108/sds/bears/AutogluonModels/ag-20240312_090653')

# 원본 데이터프레임에서 필요한 컬럼 추출
original_df = pd.read_csv("C:/Users/82108/sds/bears/original_df.csv")
selected_features = ['week', 'home', 'away', 'weather', 'temp', '강수량(mm)', '연', '월', '일', 'holiday']

form = st.form(key="my_form")
user_input = {}
for feature in selected_features:
    user_input[feature] = form.text_input(label=feature, key=feature)
submitted = form.form_submit_button()  # Update to use form_submit_button for submit

if submitted:
    # 사용자 입력값으로 새로운 데이터프레임 생성
    new_df = pd.DataFrame([user_input])
    
    # 전처리 코드 적용
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

    # 'home' 및 'away' 팀을 위한 OneHotEncoding 수동 적용
    home_columns = [f'home_{i}' for i in range(10)]  # 예시로 10개의 팀이 있다고 가정
    away_columns = [f'away_{i}' for i in range(10)]
    
    # 먼저 모든 열을 0으로 초기화
    for col in home_columns + away_columns:
        new_df[col] = 0
        
    # 사용자 입력에 해당하는 열의 값을 1로 설정
    # 'home' 및 'away' 값이 정수 형태의 문자열로 제공된다고 가정합니다.
    home_team_index = int(user_input['home'])  # 'home' 입력값을 인덱스로 변환
    away_team_index = int(user_input['away'])  # 'away' 입력값을 인덱스로 변환
    new_df[f'home_{home_team_index}'] = 1
    new_df[f'away_{away_team_index}'] = 1

    new_df.drop(['home', 'away'], axis=1, inplace=True)
    
    desired_categories_order = {'맑음':0, '구름조금':1, '구름많음':2, '흐림':3, '비':4}
    new_df['weather_encoded'] = new_df['weather'].map(desired_categories_order)
    new_df.drop(['weather'], axis=1, inplace=True)

    # 예측 수행
    prediction = model.predict(new_df)

    # 결과 출력
    st.write("예측 spec 값:", prediction)
