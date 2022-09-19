#Target 변수가 Binary이지만 균형이 맞지 않아 0과 1의 값 중 0에 몰려 있는 현상을 띤다
#Imbalanced한 상태에서는 데이터 전처리를 해주어야 한다
#0과 1중 0이 많기때문에 0의 개수를 줄여주는 것을 언더샘플링
#0과 1 중 1이 적기 때문에 1의 개수를 늘려주는 것을 오버샘플링이라 한다.
#선택은 자유이지만 오버샘플링의 경우 데이터 셋의 크기가 늘어난다는 점이 있음을 인지하자

import random
#언더샘플링 비율을 지정해주기 위하여
desired_apriori = 0.1
#target 변수의 클래스에 따른 인덱스 지정
df_train=[1,2,3,4,5]
idx_0 = df_train[df_train['target']==0].index
idx_1 = df_train[df_train['target']==1].index

#지정해준 인덱스로 클래스의 길이 지정
nb_0 = len(df_train.loc[idx_0])
nb_1 = len(df_train.loc[idx_1])

#언더샘플링 수행
undersampling_rate = ((1-desired_apriori)*nb_1)/(nb_0*desired_apriori)
undersampled_nb_0 = int(undersampling_rate*nb_0)
#target=0에 대한 언더샘플링 비율
print(undersampling_rate)
#언더샘플링 전 target = 0 의 레코드 개수
print(nb_0)
#언더샘플링 후 target = 0 의 레코드 개수
print(undersampled_nb_0)

#언더샘플링 비율이 적용된 개수만큼 랜덤하게 샘플을 뽑아서 그 인덱스 저장
undersampled_idx = random.shuffle(idx_0, random_state = 37, n_samples = undersampled_nb_0)

#언더샘플링 인덱스와 클래스 1의 인덱스를 리스트로 저장
idx_list = list(undersampled_idx)+list(idx_1)

#저장한 인덱스로 train set 인덱싱
df_train = df_train.loc[idx_list].reset_index(drop=True)
