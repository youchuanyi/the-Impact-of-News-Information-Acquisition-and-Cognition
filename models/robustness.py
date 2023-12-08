import pandas as pd
import statsmodels.api as sm
import os
current_directory = os.path.dirname(__file__)
grandparent_directory = os.path.dirname(current_directory)
print(grandparent_directory)
data_relative_path = os.path.join(grandparent_directory, 'data', 'processed')
data_file = os.path.join(data_relative_path, 'processed_data.csv')
data = pd.read_csv(data_file)
response_variable1 = 'Q10'
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

