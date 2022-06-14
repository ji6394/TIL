### 제6차 근로환경조사 분석
#### 근로자의 근로환경, 근로 자세가 근로 만족도에 미치는 영향 다중회귀분석+Anova test
``` R
install.packages('readxl')
library(readxl)
data = read_excel('work2.xlsx')

install.packages('lm.beta')
library('lm.beta')

shift = data[data$wtime_length5==1,]
table(shift$emp_type)
shift$wwa1n = shift$wwa1
shift$wwa1n[shift$wwa1n==8]=NA
shift$wwa1n[shift$wwa1n==9]=NA
shift$wwa2n = shift$wwa2
shift$wwa2n[shift$wwa2n==8]=NA
shift$wwa2n[shift$wwa2n==9]=NA
shift$wwa3n = shift$wwa3
shift$wwa3n[shift$wwa3n==8]=NA
shift$wwa3n[shift$wwa3n==9]=NA
shift$wwa4n = shift$wwa4
shift$wwa4n[shift$wwa4n==8]=NA
shift$wwa4n[shift$wwa4n==9]=NA
shift$wwa5n = shift$wwa5
shift$wwa5n[shift$wwa5n==8]=NA
shift$wwa5n[shift$wwa5n==9]=NA
shift$wbalancen = shift$wbalance
shift$wbalancen[shift$wbalance==8]= NA
shift$wbalancen[shift$wbalance==9]= NA
shift$wshiftn = shift$wshift
shift$wshiftn[shift$wshiftn==4]=NA
shift$wshiftn[shift$wshiftn==8]=NA
shift$wshiftn[shift$wshiftn==9]=NA

shift$safeinformn = shift$safeinform
shift$safeinformn[shift$safeinformn==8] = NA
shift$safeinformn[shift$safeinformn==9] = NA
shift$wtime_nightn = shift$wtime_night
shift$wtime_nightn[shift$wtime_nightn==8]=NA
shift$wtime_nightn[shift$wtime_nightn==9]=NA
shift$wtime_ftworkn = shift$wtime_ftwork
shift$wtime_ftworkn[shift$wtime_ftworkn==8]=NA
shift$wtime_ftworkn[shift$wtime_ftworkn==9]=NA
shift$wtime_ftworkn[shift$wtime_ftworkn==7]=6
shift$wsituation6n = shift$wsituation6
shift$wsituation6n[shift$wsituation6n==8]=NA
shift$wsituation6n[shift$wsituation6n==9]=NA
shift$wsituation8n = shift$wsituation8
shift$wsituation8n[shift$wsituation8n==8]=NA
shift$wsituation8n[shift$wsituation8n==9]=NA
shift$wsituation10n = shift$wsituation10
shift$wsituation10n[shift$wsituation10n==8]=NA
shift$wsituation10n[shift$wsituation10n==9]=NA
shift$wsituation12n = shift$wsituation12
shift$wsituation12n[shift$wsituation6n==8]=NA
shift$wsituation12n[shift$wsituation6n==9]=NA
shift$heal_riskn = shift$heal_risk
shift$heal_riskn[shift$heal_riskn==8]=NA
shift$heal_riskn[shift$heal_riskn==9]=NA
shift$heal_affn = shift$heal_aff
shift$heal_affn[shift$heal_affn==8]=NA
shift$heal_affn[shift$heal_affn==9]=NA
shift$heal_condn = shift$heal_cond
shift$heal_condn[shift$heal_condn==8]=NA
shift$heal_condn[shift$heal_condn==9]=NA
shift$heal_illhen = shift$heal_illhe
shift$heal_illhen[shift$heal_illhen==8]=NA
shift$heal_illhen[shift$heal_illhen==9]=NA
shift$heal_lim1n = shift$heal_lim1
shift$heal_lim1n[shift$heal_lim1n==8]=NA
shift$heal_lim1n[shift$heal_lim1n==9]=NA
shift$heal_prob1n = shift$heal_prob1
shift$heal_prob1n[shift$heal_prob1n==8]=NA
shift$heal_prob1n[shift$heal_prob1n==9]=NA
shift$heal_prob2n = shift$heal_prob2
shift$heal_prob2n[shift$heal_prob2n==8]=NA
shift$heal_prob2n[shift$heal_prob2n==9]=NA
shift$heal_prob3n = shift$heal_prob3
shift$heal_prob3n[shift$heal_prob3n==8]=NA
shift$heal_prob3n[shift$heal_prob3n==9]=NA
shift$heal_prob4n = shift$heal_prob4
shift$heal_prob4n[shift$heal_prob4n==8]=NA
shift$heal_prob4n[shift$heal_prob4n==9]=NA
shift$heal_prob5n = shift$heal_prob5
shift$heal_prob5n[shift$heal_prob5n==8]=NA
shift$heal_prob5n[shift$heal_prob5n==9]=NA
shift$heal_prob6n = shift$heal_prob6
shift$heal_prob6n[shift$heal_prob6n==8]=NA
shift$heal_prob6n[shift$heal_prob6n==9]=NA
shift$heal_prob1_1n = shift$heal_prob1_1
shift$heal_prob1_1n[shift$heal_prob1_1n==8]=NA
shift$heal_prob1_1n[shift$heal_prob1_1n==9]=NA
shift$heal_prob2_1n = shift$heal_prob2_1
shift$heal_prob2_1n[shift$heal_prob2_1n==8]=NA
shift$heal_prob2_1n[shift$heal_prob2_1n==9]=NA
shift$heal_prob3_1n = shift$heal_prob3_1
shift$heal_prob3_1n[shift$heal_prob3_1n==8]=NA
shift$heal_prob3_1n[shift$heal_prob3_1n==9]=NA
shift$heal_prob4_1n = shift$heal_prob4_1
shift$heal_prob4_1n[shift$heal_prob4_1n==8]=NA
shift$heal_prob4_1n[shift$heal_prob4_1n==9]=NA
shift$heal_prob5_1n = shift$heal_prob5_1
shift$heal_prob5_1n[shift$heal_prob5_1n==8]=NA
shift$heal_prob5_1n[shift$heal_prob5_1n==9]=NA
shift$heal_prob6_1n = shift$heal_prob6_1
shift$heal_prob6_1n[shift$heal_prob6_1n==8]=NA
shift$heal_prob6_1n[shift$heal_prob6_1n==9]=NA
shift$sleep1n = shift$sleep1
shift$sleep1n[shift$sleep1n==8]=NA
shift$sleep1n[shift$sleep1n==9]=NA
shift$sleep2n = shift$sleep2
shift$sleep2n[shift$sleep2n==8]=NA
shift$sleep2n[shift$sleep2n==9]=NA
shift$sleep3n = shift$sleep3
shift$sleep3n[shift$sleep3n==8]=NA
shift$sleep3n[shift$sleep3n==9]=NA
shift$heal_abs1n = shift$heal_abs1
shift$heal_abs1n[shift$heal_abs1n==888]=NA
shift$heal_abs1n[shift$heal_abs1n==999]=NA
shift$heal_abs2n = shift$heal_abs2
shift$heal_abs2n[shift$heal_abs2n==888]=NA
shift$heal_abs2n[shift$heal_abs2n==999]=NA
shift$heal_abs3n = shift$heal_abs3
shift$heal_abs3n[shift$heal_abs3n==888]=NA
shift$heal_abs3n[shift$heal_abs3n==999]=NA
shift$heal_wsick1n = shift$heal_wsick1
shift$heal_wsick1n[shift$heal_wsick1n==8]=NA
shift$heal_wsick1n[shift$heal_wsick1n==9]=NA
shift$heal_wsick1n[shift$heal_wsick1n==7]=2
shift$heal_wsick1n[shift$heal_wsick1n==2]=0
shift$who1n = shift$who1
shift$who1n[shift$who1n==8]=NA
shift$who1n[shift$who1n==9]=NA
shift$who2n = shift$who2
shift$who2n[shift$who2n==8]=NA
shift$who2n[shift$who2n==9]=NA
shift$who3n = shift$who3
shift$who3n[shift$who3n==8]=NA
shift$who3n[shift$who3n==9]=NA
shift$who4n = shift$who4
shift$who4n[shift$who4n==8]=NA
shift$who4n[shift$who4n==9]=NA
shift$who5n = shift$who5
shift$who5n[shift$who5n==8]=NA
shift$who5n[shift$who5n==9]=NA
shift$satisfactionn = shift$satisfaction
shift$satisfactionn[shift$satisfactionn==8]=NA
shift$satisfactionn[shift$satisfactionn==9]=NA
shift$weng1n = shift$weng1
shift$weng1n[shift$weng1n==8]=NA
shift$weng1n[shift$weng1n==9]=NA
shift$weng2n = shift$weng2
shift$weng2n[shift$weng2n==8]=NA
shift$weng2n[shift$weng2n==9]=NA
shift$weng3n = shift$weng3
shift$weng3n[shift$weng3n==8]=NA
shift$weng3n[shift$weng3n==9]=NA
shift$weng4n = shift$weng4
shift$weng4n[shift$weng4n==8]=NA
shift$weng4n[shift$weng4n==9]=NA
shift$weng5n = shift$weng5
shift$weng5n[shift$weng5n==8]=NA
shift$weng5n[shift$weng5n==9]=NA
shift$income_pos3n = shift$income_pos3
shift$income_pos3n[shift$income_pos3n==8]=NA
shift$income_pos3n[shift$income_pos3n==9]=NA
shift$income_pos4n = shift$income_pos4
shift$income_pos4n[shift$income_pos4n==8]=NA
shift$income_pos4n[shift$income_pos4n==9]=NA
shift$income_pos5n = shift$income_pos5
shift$income_pos5n[shift$income_pos5n==8]=NA
shift$income_pos5n[shift$income_pos5n==9]=NA
shift$wtime_privaten = shift$wtime_private
shift$wtime_privaten[shift$wtime_privaten==8]=NA
shift$wtime_privaten[shift$wtime_privaten==9]=NA
shift$hazard_phy1[shift$hazard_phy1==8]=NA
shift$hazard_phy1[shift$hazard_phy1==9]=NA
shift$hazard_phy2[shift$hazard_phy2==8]=NA
shift$hazard_phy2[shift$hazard_phy2==9]=NA
shift$hazard_phy3[shift$hazard_phy3==8]=NA
shift$hazard_phy3[shift$hazard_phy3==9]=NA
shift$hazard_phy4[shift$hazard_phy4==8]=NA
shift$hazard_phy4[shift$hazard_phy4==9]=NA
shift$hazard_phy5[shift$hazard_phy5==8]=NA
shift$hazard_phy5[shift$hazard_phy5==9]=NA
shift$hazard_phy6[shift$hazard_phy6==8]=NA
shift$hazard_phy6[shift$hazard_phy6==9]=NA
shift$hazard_phy7[shift$hazard_phy7==8]=NA
shift$hazard_phy7[shift$hazard_phy7==9]=NA
shift$hazard_phy8[shift$hazard_phy8==8]=NA
shift$hazard_phy8[shift$hazard_phy8==9]=NA
shift$hazard_phy9[shift$hazard_phy9==8]=NA
shift$hazard_phy9[shift$hazard_phy9==9]=NA
shift$hazard_erg1[shift$hazard_erg1==8]=NA
shift$hazard_erg1[shift$hazard_erg1==9]=NA
shift$hazard_erg2[shift$hazard_erg2==8]=NA
shift$hazard_erg2[shift$hazard_erg2==9]=NA
shift$hazard_erg3[shift$hazard_erg3==8]=NA
shift$hazard_erg3[shift$hazard_erg3==9]=NA
shift$hazard_erg4[shift$hazard_erg4==8]=NA
shift$hazard_erg4[shift$hazard_erg4==9]=NA
shift$hazard_erg5[shift$hazard_erg5==8]=NA
shift$hazard_erg5[shift$hazard_erg5==9]=NA
shift$hazard_erg6[shift$hazard_erg6==8]=NA
shift$hazard_erg6[shift$hazard_erg6==9]=NA
shift$hazard_psy1[shift$hazard_psy1==8]=NA
shift$hazard_psy1[shift$hazard_psy1==9]=NA
shift$hazard_psy2[shift$hazard_psy2==8]=NA
shift$hazard_psy2[shift$hazard_psy2==9]=NA
shift$hazard_psy3[shift$hazard_psy3==8]=NA
shift$hazard_psy3[shift$hazard_psy3==9]=NA
shift$wstat1n = shift$wstat1
shift$wstat1n[shift$wstat1n==8]=NA
shift$wstat1n[shift$wstat1n==9]=NA
shift$wstat3n = shift$wstat3
shift$wstat3n[shift$wstat3n==8]=NA
shift$wstat3n[shift$wstat3n==9]=NA
shift$woutside4n = shift$woutside4
shift$woutside4n[shift$woutside4n==8]=NA
shift$woutside4n[shift$woutside4n==9]=NA

attach(shift)
detach(shift)

shift$phymean = (shift$hazard_phy1+ shift$hazard_phy2+shift$hazard_phy3+shift$hazard_phy4+shift$hazard_phy5+shift$hazard_phy6+shift$hazard_phy7+shift$hazard_phy8+shift$hazard_phy9)/9
shift$phymean

shift$ergmean = (shift$hazard_erg1+shift$hazard_erg1+shift$hazard_erg1+shift$hazard_erg1+shift$hazard_erg1+shift$hazard_erg1+shift$hazard_erg1+)




table(shift$phymean)
s.reg1 = lm(wbalancen~wshiftn+safeinformn+wtime_nightn)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)
s.reg2 = lm(wwa1n~wshiftn+safeinformn+wtime_nightn)
s.reg2 = lm.beta(s.reg2)
summary(s.reg2)
s.reg3 = lm(wwa2n~wshiftn+safeinformn+wtime_nightn)
s.reg3 = lm.beta(s.reg3)
summary(s.reg3)
s.reg4 = lm(wwa3n~wshiftn+safeinformn+wtime_nightn)
s.reg4 = lm.beta(s.reg4)
summary(s.reg4)
s.reg5 = lm(wwa4n~wshiftn+safeinformn+wtime_nightn)
s.reg5 = lm.beta(s.reg5)
summary(s.reg5)
s.reg6 = lm(wwa5n~wshiftn+safeinformn+wtime_nightn)
s.reg6 = lm.beta(s.reg6)
summary(s.reg6)
s.reg7 = lm(wtime_ftworkn~wshiftn+safeinformn+wtime_nightn)
s.reg7 = lm.beta(s.reg7)
summary(s.reg7)
s.reg8 = lm(wsituation6n~wshiftn+safeinformn+wtime_nightn)
s.reg8 = lm.beta(s.reg8)
summary(s.reg8)
s.reg9 = lm(wsituation12n~wshiftn+safeinformn+wtime_nightn)
s.reg9 = lm.beta(s.reg9)
summary(s.reg9)
s.reg10 = lm(heal_riskn~wshiftn+safeinformn+wtime_nightn)
s.reg10 = lm.beta(s.reg10)
summary(s.reg10)
s.reg11 = lm(heal_affn~wshiftn+safeinformn+wtime_nightn)
s.reg11 = lm.beta(s.reg11)
summary(s.reg11)
s.reg12 = lm(heal_condn~wshiftn+safeinformn+wtime_nightn)
s.reg12 = lm.beta(s.reg12)
summary(s.reg12)
s.reg13 = lm(heal_illhen~wshiftn+safeinformn+wtime_nightn)
s.reg13 = lm.beta(s.reg13)
summary(s.reg13)
s.reg14 = lm(heal_lim1n~wshiftn+safeinformn+wtime_nightn)
s.reg14 = lm.beta(s.reg14)
summary(s.reg14)
s.reg15 = lm(heal_prob6n~wshiftn+safeinformn+wtime_nightn)
s.reg15 = lm.beta(s.reg15)
summary(s.reg15)
s.reg16 = lm(heal_prob6_1n~wshiftn+safeinformn+wtime_nightn)
s.reg16 = lm.beta(s.reg16)
summary(s.reg16)
s.reg17 = lm(sleep3n~wshiftn+safeinformn+wtime_nightn)
s.reg17 = lm.beta(s.reg17)
summary(s.reg17)
s.reg18 = lm(heal_abs3n~wshiftn+safeinformn+wtime_nightn)
s.reg18 = lm.beta(s.reg18)
summary(s.reg18)
s.reg19 = lm(heal_wsick1n~wshiftn+safeinformn+wtime_nightn)
s.reg19 = lm.beta(s.reg19)
summary(s.reg19)
s.reg20 = lm(who5n~wshiftn+safeinformn+wtime_nightn)
s.reg20 = lm.beta(s.reg20)
summary(s.reg20)
s.reg20 = lm(satisfactionn~wshiftn+safeinformn+wtime_nightn)
s.reg20 = lm.beta(s.reg20)
summary(s.reg20)
s.reg21 = lm(weng5n~wshiftn+safeinformn+wtime_nightn)
s.reg21 = lm.beta(s.reg21)
summary(s.reg21)
s.reg22 = lm(income_pos5n~wshiftn+safeinformn+wtime_nightn)
s.reg22 = lm.beta(s.reg22)
summary(s.reg22)

s.reg23 = lm(wbalancen~wtime_nightn)
summary(s.reg23)
s.reg23 = lm(wwa5n~wtime_nightn)
summary(s.reg23)
s.reg23 = lm(sleep3n~wtime_nightn)
summary(s.reg23)
s.reg23 = lm(wtime_privaten~wtime_nightn)
summary(s.reg23)
s.reg23 = lm(heal_condn~wtime_nightn)
summary(s.reg23)
s.reg23 = lm(sleep2n~wtime_nightn)
summary(s.reg23)

s.reg24 = lm(who4n~wtime_nightn)
summary(s.reg24)
s.reg25 = lm(satisfactionn~wtime_nightn)
summary(s.reg25)
s.reg26 = lm(weng3n~wtime_nightn)
summary(s.reg26)

s.reg27 = lm(heal_condn~safeinformn)
summary(s.reg27)
s.reg28 = lm(heal_prob1n~wtime_nightn)
summary(s.reg28)

s.reg29 = lm(heal_illhen~safeinform)
summary(s.reg29)

s.reg30 = lm(heal_lim1n~safeinform)
summary(s.reg30)
s.reg30 = lm(heal_prob6n~safeinform)
summary(s.reg30)
s.reg30 = lm(satisfactionn~safeinform)
summary(s.reg30)
table(shift$wshiftn)
table(wshiftn)
attach(shift)
table(wshiftn)
table(wtime_nightn)
a = aov(wsituation6n~wshiftn)
summary(a)
library(ggplot2)
ggplot(shift, aes(x = wshiftn,y=wsituation12n, group=wshiftn))+
  geom_boxplot()
table(wsituation6n)
wsituation6n[wsituation6n==8]=NA
table(wshiftn)
table(wsituation12n)
wsituation12n[wsituation12n==8]=NA
a = aov(wsituation12n~wshiftn)
summary(a)
ggplot(shift, aes(x= wsituation12n, fill= wshiftn))+
  geom_histogram()+
  facet_wrap(~wshiftn)
table(wsituation6n)
table(wshiftn)
a = aov(sleep3n~wshiftn)
summary(a)
ggplot(shift, aes(x= sleep3n, fill= wshiftn))+
  geom_histogram()+
  facet_wrap(~wshiftn)
g1=mean(sleep3n[wshiftn==1], na.rm=T)
g2=mean(sleep3n[wshiftn==2], na.rm=T)
g3=mean(sleep3n[wshiftn==3], na.rm=T)
g1;g2;g3
a = aov(heal_wsick1n~wshiftn)
summary(a)
ggplot(shift, aes(x= heal_wsick1n, fill= wshiftn))+
  geom_histogram()+
  facet_wrap(~wshiftn)
g1=mean(heal_wsick1n[wshiftn==1], na.rm=T)
g2=mean(heal_wsick1n[wshiftn==2], na.rm=T)
g3=mean(heal_wsick1n[wshiftn==3], na.rm=T)
g1;g2;g3
a = aov(heal_abs1n~wshiftn)
summary(a)

a = aov(who4n~wshiftn)
summary(a)
ggplot(shift, aes(x = wshiftn,y=who4n, group=wshiftn))+
  geom_boxplot()
ggplot(shift, aes(x= who4n, fill= wshiftn))+
  geom_histogram()+
  facet_wrap(~wshiftn)
ggplot(shift, aes(x= who5n, fill= wshiftn))+
  geom_histogram()+
  facet_wrap(~wshiftn)
a = aov(weng5n~wshiftn)
summary(a)
ggplot(shift, aes(x= weng3n, fill= wshiftn))+
  geom_histogram()+
  facet_wrap(~wshiftn)
#new
s.reg1 = lm(wbalancen~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)
table(wbalancen)
table(hazard_phy1)

s.reg1 = lm(wwa5n~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)

s.reg1 = lm(wtime_ftworkn~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)
table(wsituation6n)
s.reg1 = lm(satisfactionn~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)
table(hazard_erg3)
s.reg1 = lm(wstat3n~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)

s.reg1 = lm(weng5n~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)

s.reg1 = lm(woutside4n~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)

class(data)

library(car)
s.reg1 = lm(wsituation12n~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg1 = lm.beta(s.reg1)
summary(s.reg1)
dwtest(s.reg1)
vif(s.reg1)

library(gmodels)
library(lmtest)
library(lm.beta)
s.reg2 = lm(satisfactionn~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg2 = lm.beta(s.reg2)
dwtest(s.reg2)
vif(s.reg2)
summary(s.reg2)
detach(package:car)

s.reg3 = lm(wstat1n~hazard_phy1+hazard_phy2+hazard_phy2+hazard_phy3+hazard_phy4+hazard_phy5+hazard_phy6+hazard_phy7+hazard_phy8+hazard_phy9+hazard_erg1+hazard_erg2+hazard_erg3+hazard_erg4+hazard_erg5+hazard_erg6+hazard_psy1+hazard_psy2+hazard_psy3)
s.reg3= lm.beta(s.reg3)
dwtest(s.reg3)
vif(s.reg3)
summary(s.reg3)

table(wshiftn)
a = aov(who5n~wshiftn)
summary(a)
sum(table(who5n[wshiftn==1]))
sum(table(who5n[wshiftn==2]))
sum(table(who5n[wshiftn==3]))
mean(who5n[wshiftn==1], na.rm=T)
mean(who5n[wshiftn==2], na.rm=T)
mean(who5n[wshiftn==3], na.rm=T)
sd(who5n[wshiftn==1], na.rm=T)
sd(who5n[wshiftn==2], na.rm=T)
sd(who5n[wshiftn==3], na.rm=T)
library(ggplot2)
table(IND2[wshiftn==1])
table(OCC2[wshiftn==1])
sum(table(wshiftn==1))
table(OCC2[wshiftn==2])

ggplot(shift, aes(x = wshiftn,y=who5n, group=wshiftn))+
  geom_boxplot()
ggplot(shift, aes(x= who5n, fill= wshiftn))+
  geom_histogram()+
  facet_wrap(~wshiftn)
```