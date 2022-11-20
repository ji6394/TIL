import cv2
cap = cv2.VideoCapture('asmmar.mp4')
# 동영상 저장(write)

# 자신의 동영상을 불러올 파일 경로
read_path = 'asmmar.mp4'

#동영상을 저장(출력)할 파일 경로
write_path = 'intro_write.mp4'

#VideoCapture, 영상을 불러올 경로를 입력
cap = cv2.VideoCapture(read_path)

#초당 프레임 수 계산
fps = cap.get(cv2.CAP_PROP_FPS)

#프레임의 사이즈 계산
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
size = (width, height)

#VideoWriter : 동영상을 저장하는 클래스. 일련의 프레임을 동영상 파일로 저장
fourcc = cv2.VideoWriter_fourcc('M','P','4','V')
out = cv2.VideoWriter(write_path, fourcc, fps, size) #코덱 지정 : MP4V -> 확장자

#프레임 하나씩 저장하기
#불러온 파일이 정상적으로 open되어 있는지 확인
while cap.isOpened():
    
    #ret : frame을 잘 읽어왔으면 True
    # frame : 동영상의 프레임, 배열 형식
    ret, frame = cap.read()
    
    if ret:
        #영상 저장
        # (처음 out 선언 시 지정한대로, write_path에, fourcc 방식으로, fps와 size 값을 갖는 영상 저장)
        out.write(frame)
        
        #키보드 입력이 들어올때까지 1ms 기다린 후 바로 다음 프레임 읽음
        # q가 키보드 입력으로 들어오면 break
        # esc를 탈출 조건으로 하려면 OxFF==27
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
#종료
cap.release()
out.release()
cv2.destroyAllWindows()

# 동영상 저장(write)

# 자신의 동영상을 불러올 파일 경로
read_path = 'asmmar.mp4'

#동영상을 저장(출력)할 파일 경로
write_path = 'intro_write.mp4'

#VideoCapture, 영상을 불러올 경로를 입력
cap = cv2.VideoCapture(read_path)

#초당 프레임 수 계산
fps = cap.get(cv2.CAP_PROP_FPS)

#프레임의 사이즈 계산
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
size = (width, height)

#VideoWriter : 동영상을 저장하는 클래스. 일련의 프레임을 동영상 파일로 저장
fourcc = cv2.VideoWriter_fourcc('M','P','4','V')
out = cv2.VideoWriter(write_path, fourcc, fps, size) #코덱 지정 : MP4V -> 확장자

#프레임 하나씩 저장하기
#불러온 파일이 정상적으로 open되어 있는지 확인
while cap.isOpened():
    
    #ret : frame을 잘 읽어왔으면 True
    # frame : 동영상의 프레임, 배열 형식
    ret, frame = cap.read()
    
    if ret:
        #영상 저장
        # (처음 out 선언 시 지정한대로, write_path에, fourcc 방식으로, fps와 size 값을 갖는 영상 저장)
        out.write(frame)
        
        #키보드 입력이 들어올때까지 1ms 기다린 후 바로 다음 프레임 읽음
        # q가 키보드 입력으로 들어오면 break
        # esc를 탈출 조건으로 하려면 OxFF==27
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
#종료
cap.release()
out.release()
cv2.destroyAllWindows()

# 영상에 파란 직사각형 그리기
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 도형을 그릴 때 사용할 색상 (bgr 표현법)
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
# 동영상을 저장(write)할 파일 경로
write_path = "shape_write.mp4"

# VideoCapture, 기본 노트북 웹캠의 index는 0.
cap = cv2.VideoCapture('asmmar.mp4')

font = cv2.FONT_HERSHEY_COMPLEX
font_kor = ImageFont.truetype("malgun.ttf", 30)

# 초당 프레임 수 계산
fps = cap.get(cv2.CAP_PROP_FPS)

# 프레임의 사이즈 계산
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
size = (width, height)

#VideoWriter
fourcc = cv2.VideoWriter_fourcc('M','P','4','V')

# 프레임 하나씩 저장(write)하기 및 띄우기(show)
while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        cv2.rectangle(frame, (50, 200), (200,50), blue, 5)
        cv2.putText(frame, "Blue Rectangle", (50, 250), font, 1, (255,255,255))
        
        frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        #cv2.cvtColor : 회색조, 컬러이미지 변경
        #Image.fromarray : numpy(cv2) 이미지를 pil 이미지로 변경
        
        # PIL 이미지의 직사각형 위에 "파란 직사각형" 쓰기
        # 폰트의 경로를 찾지 못하는 경우 에러가 생길 수 있음
        # 새 폰트를 자신이 아는 경로에 위치시킨 후 경로의 주소를 붙여넣으면 해결됨
        draw = ImageDraw.Draw(frame_pil)
        draw.text((50,250), "파란 직사각형", font = font_kor, fill=(0,0,255))
        
        #PIL 이미지 -> cv2로 변경
        frame_np = np.array(frame_pil)
        frame = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
        
        # 이미지 띄우기
        cv2.imshow("Video_with_text", frame)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
           
#종료
cap.release()
cv2.destroyAllWindows()

# 영상 일부 잘라서 저장(write) 및 띄우기(show)

# 동영상을 저장(write)할 파일 경로
write_path = "cut_write.mp4"


# VideoCapture, 기본 노트북 웹캠의 index는 0.
cap = cv2.VideoCapture('asmmar.mp4')


# 초당 프레임 수 계산
fps = cap.get(cv2.CAP_PROP_FPS)

# 프레임의 사이즈 계산
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
size = (width, height)

# VideoWriter
fourcc = cv2.VideoWriter_fourcc('M','P','4','V')
out = cv2.VideoWriter(write_path, fourcc, fps, size)


while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        out.write(frame)
        frame_cut = frame[int(width/3):width - int(width/3), int(height/3):height - int(height/3)]
        cv2.imshow('video', frame_cut)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

# 종료
cap.release()
out.release()
cv2.destroyAllWindows()

# 웹캠 얼굴 부분 인식히기
import numpy as np
from PIL import ImageFont, ImageDraw, Image

path = "haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(path)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.05, 5)
    num = 1
    for face in faces:
        (x,y,w,h)=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255), 2)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, str(num), (x, y+30), font, 1, (0, 0, 255))
        num+=1
    cv2.imshow('face webcam', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # Esc 키를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()

#오류ㅠㅠ
from IPython.display import Image, display
import cv2
import cvlib as cv
import os
import matplotlib.pyplot as plt

real_image_index_1 = []
real_image_path_1 = []

conf = 0.5
model_name ='yolov4'

for i in range(2000):
  img = cv2.imread(image_datasets.imgs[i][0])
  result = cv.detect_common_objects(img, confidence=conf, model=model_name)
  if len(result[0]) > 1:
    real_image_index_1.append(i)
    real_image_path_1.append(image_datasets.imgs[i][0])

print("최종 구분된 실사이미지 개수: ", len(real_image_index_1))
print(real_image_index_1)
print(real_image_path_1)