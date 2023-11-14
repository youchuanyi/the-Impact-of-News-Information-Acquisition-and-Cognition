import pandas as pd
import statsmodels.api as sm
data = pd.read_csv('/Users/zhengchuyi/Desktop/the-impact-of-news-information-acquisition-and-cognition/data/processed/processed_data.csv')
print(data.head())
confirm = data['Q1']
age = data['Q2']
gender = data['Q3']
poli_afli = data['Q4']
hi_edu = data['Q5']
gra_uni = data['Q6']
hig_maj = data['Q7']
ann_inc = data['Q8']
hometown = data['Q9']
interest = data['Q13']
time = data['Q14']
overseas = data['Q15_A8']
pol_sati = data['Q10']
eco_sati = data['Q11']
lif_work_sati = data['Q12']
pol_sat = sm.OLS(pol_sati, sm.add_constant(pd.concat([age, gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time, overseas], axis=1))).fit()
eco_sati = sm.OLS(eco_sati, sm.add_constant(pd.concat([age, gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time, overseas], axis=1))).fit()
lif_work_sati = sm.OLS(lif_work_sati, sm.add_constant(pd.concat([age, gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time, overseas], axis=1))).fit()
print(pol_sat.summary())
print(eco_sati.summary())
print(lif_work_sati.summary())