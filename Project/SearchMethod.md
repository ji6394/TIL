# 근로시간의 유동성이 근로자에게 미치는 영향
# 근로시간의 유동성이 근로자의 신체적 건강, 정신적 건강, 근무 만족도에 미치는 영향을 chi-square, 교차검정, t-test를 이용하여 분석 
``` R
install.packages('readxl')
library(readxl)
data = read_excel('work2.xlsx')
library(gmodels)

data$wtime_length1n = data$wtime_length1
data$wtime_length1n[data$wtime_length1n==8]=NA
data$wtime_length1n[data$wtime_length1n==9]=NA
data$wtime_length1n[data$wtime_length1n==2]=0
table(data$wtime_length1n)
data$wtime_length2n = data$wtime_length2
data$wtime_length2n[data$wtime_length2n==8]=NA
data$wtime_length2n[data$wtime_length2n==9]=NA
data$wtime_length2n[data$wtime_length2n==2]=0
data$wtime_length3n = data$wtime_length3
data$wtime_length3n[data$wtime_length3n==8]=NA
data$wtime_length3n[data$wtime_length3n==9]=NA
data$wtime_length3n[data$wtime_length3n==2]=0
data$wtime_length4n = data$wtime_length4
data$wtime_length4n[data$wtime_length4n==8]=NA
data$wtime_length4n[data$wtime_length4n==9]=NA
data$wtime_length4n[data$wtime_length4n==2]=0
data$wtime_length5n = data$wtime_length5
data$wtime_length5n[data$wtime_length5n==8]=NA
data$wtime_length5n[data$wtime_length5n==9]=NA
data$wtime_length5n[data$wtime_length5n==2]=0

data$wwa1n = data$wwa1
data$wwa1n[data$wwa1n==8]=NA
data$wwa1n[data$wwa1n==9]=NA
data$wwa2n = data$wwa2
data$wwa2n[data$wwa2n==8]=NA
data$wwa2n[data$wwa2n==9]=NA
data$wwa3n = data$wwa3
data$wwa3n[data$wwa3n==8]=NA
data$wwa3n[data$wwa3n==9]=NA
data$wwa4n = data$wwa4
data$wwa4n[data$wwa4n==8]=NA
data$wwa4n[data$wwa4n==9]=NA
data$wwa5n = data$wwa5
data$wwa5n[data$wwa5n==8]=NA
data$wwa5n[data$wwa5n==9]=NA
data$wbalancen = data$wbalance
data$wbalancen[data$wbalance==8]= NA
data$wbalancen[data$wbalance==9]= NA
data$wshiftn = data$wshift
data$wshiftn[data$wshiftn==4]=NA
data$wshiftn[data$wshiftn==8]=NA
data$wshiftn[data$wshiftn==9]=NA

data$safeinformn = data$safeinform
data$safeinformn[data$safeinformn==8] = NA
data$safeinformn[data$safeinformn==9] = NA
data$wtime_nightn = data$wtime_night
data$wtime_nightn[data$wtime_nightn==8]=NA
data$wtime_nightn[data$wtime_nightn==9]=NA
data$wtime_ftworkn = data$wtime_ftwork
data$wtime_ftworkn[data$wtime_ftworkn==8]=NA
data$wtime_ftworkn[data$wtime_ftworkn==9]=NA
data$wtime_ftworkn[data$wtime_ftworkn==7]=6
data$wsituation6n = data$wsituation6
data$wsituation6n[data$wsituation6n==8]=NA
data$wsituation6n[data$wsituation6n==9]=NA
data$wsituation8n = data$wsituation8
data$wsituation8n[data$wsituation8n==8]=NA
data$wsituation8n[data$wsituation8n==9]=NA
data$wsituation10n = data$wsituation10
data$wsituation10n[data$wsituation10n==8]=NA
data$wsituation10n[data$wsituation10n==9]=NA
data$wsituation12n = data$wsituation12
data$wsituation12n[data$wsituation12n==8]=NA
data$wsituation12n[data$wsituation12n==9]=NA
data$heal_riskn = data$heal_risk
data$heal_riskn[data$heal_riskn==8]=NA
data$heal_riskn[data$heal_riskn==9]=NA
data$heal_affn = data$heal_aff
data$heal_affn[data$heal_affn==8]=NA
data$heal_affn[data$heal_affn==9]=NA
data$heal_condn = data$heal_cond
data$heal_condn[data$heal_condn==8]=NA
data$heal_condn[data$heal_condn==9]=NA
data$heal_illhen = data$heal_illhe
data$heal_illhen[data$heal_illhen==8]=NA
data$heal_illhen[data$heal_illhen==9]=NA
data$heal_lim1n = data$heal_lim1
data$heal_lim1n[data$heal_lim1n==8]=NA
data$heal_lim1n[data$heal_lim1n==9]=NA
data$heal_prob1n = data$heal_prob1
data$heal_prob1n[data$heal_prob1n==8]=NA
data$heal_prob1n[data$heal_prob1n==9]=NA
data$heal_prob2n = data$heal_prob2
data$heal_prob2n[data$heal_prob2n==8]=NA
data$heal_prob2n[data$heal_prob2n==9]=NA
data$heal_prob3n = data$heal_prob3
data$heal_prob3n[data$heal_prob3n==8]=NA
data$heal_prob3n[data$heal_prob3n==9]=NA
data$heal_prob4n = data$heal_prob4
data$heal_prob4n[data$heal_prob4n==8]=NA
data$heal_prob4n[data$heal_prob4n==9]=NA
data$heal_prob5n = data$heal_prob5
data$heal_prob5n[data$heal_prob5n==8]=NA
data$heal_prob5n[data$heal_prob5n==9]=NA
data$heal_prob6n = data$heal_prob6
data$heal_prob6n[data$heal_prob6n==8]=NA
data$heal_prob6n[data$heal_prob6n==9]=NA
data$heal_prob1_1n = data$heal_prob1_1
data$heal_prob1_1n[data$heal_prob1_1n==8]=NA
data$heal_prob1_1n[data$heal_prob1_1n==9]=NA
data$heal_prob2_1n = data$heal_prob2_1
data$heal_prob2_1n[data$heal_prob2_1n==8]=NA
data$heal_prob2_1n[data$heal_prob2_1n==9]=NA
data$heal_prob3_1n = data$heal_prob3_1
data$heal_prob3_1n[data$heal_prob3_1n==8]=NA
data$heal_prob3_1n[data$heal_prob3_1n==9]=NA
data$heal_prob4_1n = data$heal_prob4_1
data$heal_prob4_1n[data$heal_prob4_1n==8]=NA
data$heal_prob4_1n[data$heal_prob4_1n==9]=NA
data$heal_prob5_1n = data$heal_prob5_1
data$heal_prob5_1n[data$heal_prob5_1n==8]=NA
data$heal_prob5_1n[data$heal_prob5_1n==9]=NA
data$heal_prob6_1n = data$heal_prob6_1
data$heal_prob6_1n[data$heal_prob6_1n==8]=NA
data$heal_prob6_1n[data$heal_prob6_1n==9]=NA
data$sleep1n = data$sleep1
data$sleep1n[data$sleep1n==8]=NA
data$sleep1n[data$sleep1n==9]=NA
data$sleep2n = data$sleep2
data$sleep2n[data$sleep2n==8]=NA
data$sleep2n[data$sleep2n==9]=NA
data$sleep3n = data$sleep3
data$sleep3n[data$sleep3n==8]=NA
data$sleep3n[data$sleep3n==9]=NA
data$heal_abs1n = data$heal_abs1
data$heal_abs1n[data$heal_abs1n==888]=NA
data$heal_abs1n[data$heal_abs1n==999]=NA
data$heal_abs2n = data$heal_abs2
data$heal_abs2n[data$heal_abs2n==888]=NA
data$heal_abs2n[data$heal_abs2n==999]=NA
data$heal_abs3n = data$heal_abs3
data$heal_abs3n[data$heal_abs3n==888]=NA
data$heal_abs3n[data$heal_abs3n==999]=NA
data$heal_wsick1n = data$heal_wsick1
data$heal_wsick1n[data$heal_wsick1n==8]=NA
data$heal_wsick1n[data$heal_wsick1n==9]=NA
data$heal_wsick1n[data$heal_wsick1n==7]=2
data$heal_wsick1n[data$heal_wsick1n==2]=0
data$who1n = data$who1
data$who1n[data$who1n==8]=NA
data$who1n[data$who1n==9]=NA
data$who2n = data$who2
data$who2n[data$who2n==8]=NA
data$who2n[data$who2n==9]=NA
data$who3n = data$who3
data$who3n[data$who3n==8]=NA
data$who3n[data$who3n==9]=NA
data$who4n = data$who4
data$who4n[data$who4n==8]=NA
data$who4n[data$who4n==9]=NA
data$who5n = data$who5
data$who5n[data$who5n==8]=NA
data$who5n[data$who5n==9]=NA
data$satisfactionn = data$satisfaction
data$satisfactionn[data$satisfactionn==8]=NA
data$satisfactionn[data$satisfactionn==9]=NA
data$weng1n = data$weng1
data$weng1n[data$weng1n==8]=NA
data$weng1n[data$weng1n==9]=NA
data$weng2n = data$weng2
data$weng2n[data$weng2n==8]=NA
data$weng2n[data$weng2n==9]=NA
data$weng3n = data$weng3
data$weng3n[data$weng3n==8]=NA
data$weng3n[data$weng3n==9]=NA
data$weng4n = data$weng4
data$weng4n[data$weng4n==8]=NA
data$weng4n[data$weng4n==9]=NA
data$weng5n = data$weng5
data$weng5n[data$weng5n==8]=NA
data$weng5n[data$weng5n==9]=NA
data$income_pos3n = data$income_pos3
data$income_pos3n[data$income_pos3n==8]=NA
data$income_pos3n[data$income_pos3n==9]=NA
data$income_pos4n = data$income_pos4
data$income_pos4n[data$income_pos4n==8]=NA
data$income_pos4n[data$income_pos4n==9]=NA
data$income_pos5n = data$income_pos5
data$income_pos5n[data$income_pos5n==8]=NA
data$income_pos5n[data$income_pos5n==9]=NA
data$wtime_privaten = data$wtime_private
data$wtime_privaten[data$wtime_privaten==8]=NA
data$wtime_privaten[data$wtime_privaten==9]=NA
data$hazard_phy1[data$hazard_phy1==8]=NA
data$hazard_phy1[data$hazard_phy1==9]=NA
data$hazard_phy2[data$hazard_phy2==8]=NA
data$hazard_phy2[data$hazard_phy2==9]=NA
data$hazard_phy3[data$hazard_phy3==8]=NA
data$hazard_phy3[data$hazard_phy3==9]=NA
data$hazard_phy4[data$hazard_phy4==8]=NA
data$hazard_phy4[data$hazard_phy4==9]=NA
data$hazard_phy5[data$hazard_phy5==8]=NA
data$hazard_phy5[data$hazard_phy5==9]=NA
data$hazard_phy6[data$hazard_phy6==8]=NA
data$hazard_phy6[data$hazard_phy6==9]=NA
data$hazard_phy7[data$hazard_phy7==8]=NA
data$hazard_phy7[data$hazard_phy7==9]=NA
data$hazard_phy8[data$hazard_phy8==8]=NA
data$hazard_phy8[data$hazard_phy8==9]=NA
data$hazard_phy9[data$hazard_phy9==8]=NA
data$hazard_phy9[data$hazard_phy9==9]=NA
data$hazard_erg1[data$hazard_erg1==8]=NA
data$hazard_erg1[data$hazard_erg1==9]=NA
data$hazard_erg2[data$hazard_erg2==8]=NA
data$hazard_erg2[data$hazard_erg2==9]=NA
data$hazard_erg3[data$hazard_erg3==8]=NA
data$hazard_erg3[data$hazard_erg3==9]=NA
data$hazard_erg4[data$hazard_erg4==8]=NA
data$hazard_erg4[data$hazard_erg4==9]=NA
data$hazard_erg5[data$hazard_erg5==8]=NA
data$hazard_erg5[data$hazard_erg5==9]=NA
data$hazard_erg6[data$hazard_erg6==8]=NA
data$hazard_erg6[data$hazard_erg6==9]=NA
data$hazard_psy1[data$hazard_psy1==8]=NA
data$hazard_psy1[data$hazard_psy1==9]=NA
data$hazard_psy2[data$hazard_psy2==8]=NA
data$hazard_psy2[data$hazard_psy2==9]=NA
data$hazard_psy3[data$hazard_psy3==8]=NA
data$hazard_psy3[data$hazard_psy3==9]=NA
data$wstat1n = data$wstat1
data$wstat1n[data$wstat1n==8]=NA
data$wstat1n[data$wstat1n==9]=NA
data$wstat3n = data$wstat3
data$wstat3n[data$wstat3n==8]=NA
data$wstat3n[data$wstat3n==9]=NA
data$woutside4n = data$woutside4
data$woutside4n[data$woutside4n==8]=NA
data$woutside4n[data$woutside4n==9]=NA

attach(data)

chisq.test(heal_prob6n, wtime_length1n)
CrossTable(wtime_length1n, heal_prob6n)


t.test(wsituation12n~wtime_length1n)
a=wsituation12n[wtime_length1n==0]
b=wsituation12n[wtime_length1n==1]
c=table(wsituation12n[wtime_length1n==0])
d=table(wsituation12n[wtime_length1n==1])
e = prop.table(c)
f=prop.table(d)
par(mfrow=c(1,2))
barplot(e)
barplot(f)
sd(a, na.rm=T)
sd(b, na.rm=T)
c
d
summary(a)
summary(b)

t.test(wbalancen~wtime_length1n)
a=wbalancen[wtime_length1n==0]
b=wbalancen[wtime_length1n==1]
c=table(wbalancen[wtime_length1n==0])
d=table(wbalancen[wtime_length1n==1])
e = prop.table(c)
f=prop.table(d)
par(mfrow=c(1,2))
barplot(e)
barplot(f)
sd(a, na.rm=T)
sd(b, na.rm=T)
c
d
summary(a)
summary(b)

chisq.test(heal_prob6n, wtime_length2n)
CrossTable(wtime_length2n, heal_prob6n)


t.test(wsituation12n~wtime_length2n)
a=wsituation12n[wtime_length2n==0]
b=wsituation12n[wtime_length2n==1]
c=table(wsituation12n[wtime_length2n==0])
d=table(wsituation12n[wtime_length2n==1])
e = prop.table(c)
f=prop.table(d)
par(mfrow=c(1,2))
barplot(e)
barplot(f)
sd(a, na.rm=T)
sd(b, na.rm=T)
c
d
summary(a)
summary(b)

t.test(wbalancen~wtime_length2n)
a=wbalancen[wtime_length2n==0]
b=wbalancen[wtime_length2n==1]
c=table(wbalancen[wtime_length2n==0])
d=table(wbalancen[wtime_length2n==1])
e = prop.table(c)
f=prop.table(d)
par(mfrow=c(1,2))
barplot(e)
barplot(f)
sd(a, na.rm=T)
sd(b, na.rm=T)
c
d
summary(a)
summary(b)
```