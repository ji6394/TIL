## 트렌드프로그래밍 2주차
``` R
9%/%6 #몫
round(1.45648, digits = 2) #반올림, digits는 자리수
ceiling(3.60) #올림
floor(3.60) #내림
trunc(5.12) #버림

log(100) #자연로그 100
log2(8)

a = c(1,2,3,4)
b = c(5,6,7)
a + b #길이가 짧은 벡터가 반복되지만 경고 메시지 뜸

str(x) #string 아님! structure로 데이터의 구조 반환
length(x) #데이터의 길이
seq(1,10,2) #반복

rep(1:10, times = 3) #해당 요소 반복하여 출력
paste(벡터1,벡터2,팩터1) #서로 다른 str일지라도 붙여줌
x1 = c(seq(2,10,2))
x1[-2] #2번째 요소 제외하고 리턴

bokpage = c(300,250,330,270,280,310,275,290)
quantile(bookpage) #전체의 1/4,2/4,3/4지점의 값 프린트
IQR(bookpage) #Q3-Q1
var(bookpage) #분산
sd(bookpage) #표준편차
range(bookpage) #최소값 최대값 출력
diff(range(bookpage)) #최소값 최대값 차이

x = list(name='tom',age=20,toeic=c(850,890)) #리스트 내 변수의 이름 설정 가능
x$name
x$age
x$toeic

x1 = matrix(1:20,nrows=4, ncols=5,byrow=T) #byrow=T : 행방향으로 입력

x = 1:4
y = 2:5
n1 = cbind(x,y) #열방향으로 column x 와 y 합함
n2 = rbind(x,y)

score = matrix(c(100,80,75,77,83,90,70,60,59,88,98,82), nrow=4, ncol = 3)
rownames(score) = c('소연','소현','지호','한결')
colnames(score) = c('math','englsih','coding')
#rownames와 colnames로 행과 열의 이름 설정 가능
score['소연','coding']

x=c(6,3,7,6,2,9,2,5)
sort(x) #오름차순으로 정렬
sort(x,descending=T) #내림차순으로 정렬

#apply함수
apply(score,1,sum) #각 행의 sum
apply(score,2,sum) #각 열의 sum

x1=c(1,2,3)
x2=c(4,5,6,7,8)
xy = list(x1,y1)
sapply(xy,sum) #길이가 서로 다른 벡터는 계산이 안되지만 sapply는 각 벡터끼리 각각 계산해줌

#dataframe 만들기
x1 = c(1,2,3,4)
x2 = c(90,80,70,60)
a = data.frame(x1,x2)
dim(a) #a의 행과 열 출력

colSums(a) #행의 합
colMeans(a)
rowSums(a)
rowMeans(a)

r.class$toeic #dataframe에서의 indexing. matrix에서는 matrix[2,]
r.class$age = NULL #해당 열을 없앰
r.class$pass = ifelse(r.class$t_mean>=900,'Y','N')

hist(cars$speed, col='red')
plot(cars$speed, cars$dist) #산점도
abline(cars$speed, cars$dist, col = 'red') #데이터에 기반한 추세선(회귀선)

head(state.x77) #맨 위 6줄
tail(state.x77) #맨 아래 6줄
state = data.frame(state.x77)
names(state) #변수 이름 출력
colMeans(state) #모든 열의 평균값
summary(state$Income)




