import os
import pandas as pd
current_directory = os.path.dirname(__file__)
grandparent_directory = os.path.dirname(os.path.dirname(current_directory))
data_relative_path = os.path.join(grandparent_directory, 'data', 'processed')
data_file = os.path.join(data_relative_path, 'processed_data.csv')
data = pd.read_csv(data_file)
description = data.describe()
print(description)

