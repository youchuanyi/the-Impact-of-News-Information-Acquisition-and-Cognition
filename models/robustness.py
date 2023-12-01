import pandas as pd
import statsmodels.api as sm

data = pd.read_csv('/Users/zhengchuyi/Desktop/the-impact-of-news-information-acquisition-and-cognition/data/processed/processed_data.csv')

response_variable1 = 'Q10'
predictors1 = ['Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q13', 'Q14', 'Q15_A8']

mlogit_model1 = sm.MNLogit(data[response_variable1], sm.add_constant(data[predictors1]))
result1 = mlogit_model1.fit()
print(result1.summary())

response_variable2 = 'Q11'
predictors2 = ['Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q13', 'Q14', 'Q15_A8']

mlogit_model2 = sm.MNLogit(data[response_variable2], sm.add_constant(data[predictors2]))
result2 = mlogit_model2.fit()
print(result2.summary())

response_variable3 = 'Q12'
predictors3 = ['Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q13', 'Q14', 'Q15_A8']

mlogit_model3 = sm.MNLogit(data[response_variable3], sm.add_constant(data[predictors3]))
result3 = mlogit_model3.fit()
print(result3.summary())

