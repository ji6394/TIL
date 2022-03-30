## FORIF 스터디 week1
``` python
!pip install riotwatcher
import pandas as pd
import matplotlib.pyplot as plt
from riotwatcher import LolWatcher #Riot Api에 데이터 요청

api_key = 'RGAPI-56bd271d-5008-41d9-a0c8-b3391dd59f35' #Riotwatcher 키 변수에 저장
watcher = LolWatcher(api_key)

#버전 확인
version = watcher.data_dragon.versions_for_region('kr') #한국 서버, data_dragon 은 일종의 DB에 해당
champions_version = version['n']['champion']

latest = watcher.data_dragon.versions_for_region('kr')['n']['champion']
static_champ_list = watcher.data_dragon.champions(latest,False,'ko_KR')
static_champ_data = static_champ_list['data']
champ_list = static_champ_data.keys()
champ_data = [] #빈 리스트?
champ_stat = list(static_champ_data['Aatrox']['stats'].keys()) #왜 리스트로 넣어야하지??
info_key = list(static_champ_data['Aatrox']['info'].keys()) #왜 리스트??


## 데이터 만들기
for champ in champ_list :
    temp = []
    temp.append(static_champ_data[champ]['id'])
    for stat in champ_stat :
        temp.append(static_champ_data[champ]['stats'][stat])
    if len(static_champ_data['tags'])>1:
        temp.append(static_champ_data[champ]['tags'][0])
        temp.append(static_champ_data[champ]['tags'][1])
    else :
        temp.append(static_champ_data[champ]['tags'][0])
        temp.append(None)
    for info in info_key : 
        temp.append(static_champ_data[champ]['info'][info])
    champ_data.append(temp)

my_col = ['id'] +['primary_class', 'secondary_class', 'info_attack', 'info_defense', 'info_magic', 'info_difficulty']+ champ_stat #칼럼을 만드는 작업. 리스트로 넣어야 데이터프레임의 칼럼으로 넣을 수 있는듯!, 순서 맞춰서 써야함!!

champ_data = pd.DataFrame(champ_data, index = champ_list, columns = my_col)

champ_data.head()
champ_data.info()
champ_data
champ_data.shape #행과 열
champ_data.values #값만 출력
champ_data.columns #열 이름 출력
champ_data.index #행 이름 출력

# 데이터프레임에서 특정 열을 기준으로 정렬하기
champ_hp = champ_data.sort_values('hp',ascending=False) #내림차순
champ_as = champ_data.sort_values('attackspeed',ascending=False)
champ_hp_diff = champ_data.sort_values(['hp','info_difficulty'],ascending = [False, True]) #여러 열을 기준으로 정렬할 때에는 리스트 사용

#데이터프레임 조건 사용하여 인덱싱
tank_gt_600 = champ_data[(champ_data['hp']>600) & (champ_data['primary_class']=='Tank')]

deal_tang = ['Fighter','Tank']
class_dealTang = champ_data[champ_data['primary_class'].isin(deal_tang)] #isin 사용하여 인덱싱

#Query함수 사용하여 인덱스 검색
champ_data.query("primary_class == 'Tank'")
champ_data.query("primary_class == 'Tank' and info_difficulty <6")

#예시 문제1 : 18레벨의 공격력을 구하여 max_attack열을 만들어 입력

champ_data['max_attack'] = champ_data['attackdamage'] + champ_data['attackdamageperlevel']*(18-1) * (0.7025+0.0175*(18-1))

#Group_by 사용하기
champ_data.groupby('primary_class').mean()
#Groupby는 객체로 취급되어 출력되지 않음. Groupby를 사용하기 위해서는 연산을 가해야 함
#Aggregate를 통해 원하는 열에 한해 함수 사용 가능, 함수 하나를 쓸 때는 굳이 aggregate사용할 필요가 없으나 여러 함수를 사용할 때는 agg 사용해야함
champ_data.groupby('primary_class')['hp','armor','attackdamage','attackspeed'].agg('mean')
champ_data.groupby('primary_class')['hp','armor','attackdamage','attackspeed'].agg(['mean','median'])
#3.3.3 연습 : 근접 역할군의 챔피언 중 쉬운것은?
#1. 근접 역할군 (Tank, Fighter, Assassin) 챔피언만 추출 (query, [] 등등....)
#    1. `primary_class` 또는 `secondary_class` 가 근접 역할군
#2. 해당하는 챔피언을 다음의 기준 순으로 정렬
#    1. `difficulty`  : 오름차순 (True)
#    2. `hp`  : 내림차순 (False)
#    3. `DPS`  : 내림차순

short = ['Tank','Fighter','Assasin']
shortchamp = champ_data.query('primary_class == @short or secondary_class == @short') #쿼리를 사용할 때 외부 객체를 언급할때는 @ 사용하면 됨

short_champ_sorted = shortchamp.sort_values(['info_difficulty','hp','DPS'], ascending = [True,False,False])

diff_zero = short_champ_sorted[short_champ_sorted['difficulty']==0].index #index는 해당 행의 숫자 리턴

short_champ_sorted = short_champ_sorted.drop(diff_zero)

#3.3.4 연습 : 쉬운 챔피언일수록 체력이 높을까?

diffhp = champ_data.groupby('difficulty')['max_hp','max_armor'].agg('mean')

#파일 저장
from google.colab import drive
drive.mount('/content/gdrive')

champ_data.to_csv('/content/gdrive/MyDrive/Colab Notebooks/champ_data.csv')

#파일 읽기
temptemp = pd.read_csv('/content/gdrive/Mydrive/Colab Notebooks/champ_data.csv')