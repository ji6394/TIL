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
plot(state$HS.Grad, state$Income)
x1 = lm(state$HS.Grad~state$Income) #lm(x:독립변수~y:종속변수)
which.max(state$Income) #해당 열에서 가장 높은 행의 인덱스 리턴

```
#### 트렌드프로그래밍 3주차
``` R 
order(state$Population) #해당 열에서 크기에 따른 순서 인덱스 리턴
#filter 특정 조건에 맞는 행 추출
mtcars %>%
  filter(hp>150)
mtcars %>%
  filter(cyl ==6 | am ==1)
mtcars%>%
  filter(cyl == 6 & am ==1 & vs ==0)

mtcars %>%
  filter(gear %in% c(4,5)) #gear가 4,5인 행 모두 출력
mean(state$Murder)
state %>%
  filter(Murder>8) #Murder이 일정 이상 높은 주를 찾자!

#select 특정 열 추출
mtcars[,c(3,5)]
mtcars[,'cyl']

mtcars_df <- mtcars %>%
  select(mpg,cyl) #mpg, cyl변수 열만 추출!
mtcars_df

#특정 열 기준 오름차순 정렬 arrange
mtcars_df %>%
arrange(mpg,cyl) #mpg기준으로 오름차순 정렬 여기 에러뜸!!!!!!!!
mtcars_df
table(mtcars$cyl)
a <- mtcars_df %>%
  group_by(cyl) %>%
  summarise(mpg평균 = mean(mpg))
a
View(iris)
table(iris$Species)
b <- iris %>%
  group_by(Species) %>%
  summarise(SL평균=mean(Sepal.Length))
b

women
mutate(women, h.cm = height*2.54, w.kg = weight*0.45) #필요한 열을 추가하고 싶을 때 사용


View(Orange)
table(Orange$Tree)
Oranmean = Orange %>%
  group_by(Tree) %>%
  summarise(age평균=mean(circumference))
Oranmean
```
## 트렌드프로그래밍 4주차
``` R
#원하는 열 추출
subset(iris, select=c(Sepal.Length, sepal.Length))
#원하는 행 추출
subset(iris, Species=='versicolor')
#조건에 맞는 값만 출력하기
subset(iris, Petal.Width>2 |Petal.Length>6, select=c(Petal.Length, Petal.Width))

#특정 열 기준 오름차순 정렬
mtcars %>% arrange(mpg,cyl)
mtcars %>% arrange(desc(mpg))

#데이터 합치기 merge
a = data.frame(id=c(1,2,3),math1=c(80,75,90))
b = data.frame(id=c(1,2,3),math2=c(50,30,90))
merge(a,b,by='id')
# 데이터 합치기 cbind, rbind
cbind(a,b) #merge와 달리 그냥 다 붙여버림
rbind(a,b) #동일한 열이 있을 경우 불가능

#데이터 분리하기 split
split(iris, iris$Species) #Species를 기준으로 iris 분리

#히스토그램 제목, x축y축 이름 등 설정하기
hist(cars$dist, main = '자동차의 제동거리', xlab='제동거리', ylab = '빈도수', border = 'blue',col='gold',breaks=10)

table(iris$Species) #빈도값 나타내줌

#막대그래프 그리기
barplot(a,main='Species of iris', xlab='species', ylab = 'frequency', col='tan')

#박스 그림 그리기
boxplot(iris1)
boxplot(Sepal.Length ~ Species, data = iris, main = 'Length Result', col = c('red','blue','purple'))

x=c(1:10)
y=c(5:15)
boxplot(x,y,col='oldlace', names=c('x','y'))
boxplot(circumference~Tree, data = Orange, main = '나무의 둘레', col='cyan')

#그래프 그릴 때 범위 설정해주기
x=1:10
y1=log(x)
y2=sqrt(x)
plot(x,y1,ylim=c(0,4),type='l',col='red')
lines(x,y2,lty=5, col='blue')

#axis로 축 설정 변경하기
x = c(100,200,180,150,160)
y=c(220,300,280,190,240)
z=c(310,330,320,290,220)
plot(x, type='o',col='red',ylim=c(0,400),axes=F, ann=F) 
axis(1,at=1:5, lab=c('A','B','C','D','E'))
axis(2,ylim = c(0,400))
#plot으로 그래프 그린다음 lines로 그래프에 추가 가능
lines(y, type='b', pch=17, col='green',lty=5)
title(main='book page', col.main='purple')
title(xlab='book',ylab='page',col.lab='grey')
# 주석 만들기(cex는 글자크기, pch와 lty는 점모양과 선모양)
legend(4,500,c('sci','Eng','math'), cex=0.5, col=c('red','green','blue'), pch=21, lty=1)

#누적도수분포표 만들기
class = margin.table(Titanic, margin=1) #1열의 데이터로 누적도수분포표 생성
pie(class)
pie(class,labels=c(325,285,706,885), main = 'Titanic passengers')
#text로 pie차트에 문구 새겨놓기
text(0.4,0.2,"1등석")
text(0.2,0.6,'2등석')
text(-0.5,0.1,'3등석')
text(0.1,-0.3,'crew')

barplot(class, horiz=T, xlab='FerryClass', ylab='Frequency', main = 'PassengersByClass', col='blue') #가로 막대그래프그리기

#특정 열에 대한 행의 누적도수분포표 그리기
survive.by.class = margin.table(Titanic, margin = c(1,4))

barplot(survive.by.class,beside=T, col=c('black','green'), legend=T, names.arg = c('1등석','2등석','3등석','선원'))
#beside는 각 변수를 독립적으로 그려줌, names.arg또는 names로 x축 변량에 이름 넣을 수 있음

#원형그래프그리기
symbols(state$HS.Grad, state$Income, circles=state$Population, inches=0.7, fg='black', bg='salmon', lwd=1, xlab='고졸비율',ylab='1인당소득',main='고졸비율과소득')

#par mfrow로 화면분활하기
plot(1:20)
plot(20:1)
par(mfrow=c(1,3))
```