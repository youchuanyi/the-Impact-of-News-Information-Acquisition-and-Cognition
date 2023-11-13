import numpy as np
import pandas as pd
import os
current_directory = os.path.dirname(__file__)
grandparent_directory = os.path.dirname(os.path.dirname(current_directory))
data_relative_path = os.path.join(grandparent_directory, 'data', 'interim')
data_file = os.path.join(data_relative_path, 'data.csv')
data = pd.read_csv(data_file)
index_of_valid_column = data.columns.get_loc('Q31')
index_of_time_column = data.columns.get_loc('time')
columns_to_keep = list(range(4, 27)) + [index_of_valid_column]+[index_of_time_column]
data = data[data.columns[columns_to_keep]]
#drop invalid sample
data = data[data['Q31']==7]
data = data[data['time']>7]
data = data.drop(columns=['Q15_A3','Q15_A4','Q15_A5','Q15_A6','Q15_A7','Q15_A9','Q15_A10','Q15_A10_open'])

#data restore
data_relative_path_output = os.path.join(grandparent_directory, 'data', 'processed')
file_path = os.path.join(data_relative_path_output, 'processed_data.csv')
data.to_csv(file_path, index=False)






