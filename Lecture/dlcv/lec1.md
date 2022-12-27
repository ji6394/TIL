## Object detection
 - Localization : 단 하나의 object위치를 bounding box를 활용하여 찾음
 - Detection : 여러개의 object 위치를 bounding box를 활용하여 찾음
 - Segmentation : 여러개의 object 위치를 pixel 단위로 찾음
## Object detection의 난제
 - classification과 Regression을 동시에 진행해야 함
 - 다양한 크기와 유형의 object가 혼재
 - Detect 시간도 신경써야함
 - 이미지가 명확하지 않을 수도 있음
 - 데이터 세트가 부족하고 annotation을 만들어야 하므로 훈련 데이터 셋을 만들기 상대적으로 어려움