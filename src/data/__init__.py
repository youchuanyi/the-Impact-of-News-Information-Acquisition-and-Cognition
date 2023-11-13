import numpy as np
import pandas as pd
import os
current_directory = os.path.dirname(__file__)
grandparent_directory = os.path.dirname(os.path.dirname(current_directory))
data_relative_path = os.path.join(grandparent_directory, 'data', 'interim')
data_file = os.path.join(data_relative_path, 'data.csv')
data = pd.read_csv(data_file)
columns_to_remove = ['']



