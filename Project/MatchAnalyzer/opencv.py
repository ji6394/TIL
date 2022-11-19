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
        