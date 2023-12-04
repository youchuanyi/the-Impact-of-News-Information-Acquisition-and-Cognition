import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
current_directory = os.path.dirname(__file__)
grandparent_directory = os.path.dirname(os.path.dirname(current_directory))
data_relative_path = os.path.join(grandparent_directory, 'data', 'processed')
data_file = os.path.join(data_relative_path, 'processed_data.csv')
data = pd.read_csv(data_file)
pd.set_option('display.max_columns', None)
description = data.describe()
print(description)
sns.set(style="whitegrid")
#fig for control
fig, axes1 = plt.subplots(2, 4, figsize=(20, 10), constrained_layout=True)
#q3
gender_mapping = {1: 'Male', 2: 'Female'}
data['Q3_mapped'] = data['Q3'].map(gender_mapping)
sns.countplot(x='Q3_mapped', data=data,ax=axes1[0,0])
axes1[0, 0].set_title('Q3 gender')
axes1[0, 0].set_xlabel('Gender')
axes1[0, 0].set_ylabel('Frequency')

#q4
PA_mapping = {1:'General public',2:'Communist \nParty',3:'Democratic \nParties',4:'Communist \nYouth League'}
data['Q4_mapped'] = data['Q4'].map(PA_mapping)
sns.countplot(x='Q4_mapped', data=data,ax=axes1[0,1])
axes1[0, 1].set_title('Q4 Political Affiliation')
axes1[0, 1].set_xlabel('Political affiliation')
axes1[0, 1].set_ylabel('Frequency')
axes1[0, 1].tick_params(axis='x', labelsize=7)

#q5
Education_mapping = {1:'Junior college', 2: 'Bachelor', 3: 'Master or higher'}
data['Q5_mapped']=data['Q5'].map(Education_mapping)
sns.countplot(x='Q5_mapped', data=data,ax=axes1[0,2])
axes1[0, 2].set_title('Q5 highest educational attainment')
axes1[0, 2].set_xlabel('education')
axes1[0, 2].set_ylabel('Frequency')
axes1[0, 2].tick_params(axis='x', labelsize=7)

#q6
University_mapping = {1: '985-tier \nuniversity',2: '211-tier \nuniversity',3:'General \ninstitution', 4:'Vocational college \nor higher vocational \ninstitution'}
data['Q6_mapped']=data['Q6'].map(University_mapping)
sns.countplot(x='Q6_mapped', data=data,ax=axes1[0,3])
axes1[0, 3].set_title('Q6 category of the university')
axes1[0, 3].set_xlabel('Category of the university')
axes1[0, 3].set_ylabel('Frequency')
axes1[0, 3].tick_params(axis='x', labelsize=7)
#q7
Major_mapping = {1: 'Humanities \nand Arts',2: 'Social \nSciences',3: 'Science and \nEngineering',4: 'Agriculture, \nAnimal Husbandry, \nMedicine'}
data['Q7_mapped']=data['Q7'].map(Major_mapping)
sns.countplot(x='Q7_mapped', data=data,ax=axes1[1,0])
axes1[1, 0].set_title('Q7 Major')
axes1[1, 0].set_xlabel('Major')
axes1[1, 0].set_ylabel('Frequency')
axes1[1, 0].tick_params(axis='x', labelsize=7)
#q8
Income_mapping = {1: 'Below 20k',2: '20k\n-50k' ,3: '50k\n-100k',4: '100k\n-150k',5: '150k\n-200k',
                  6:'200k\n-400k',7: '400k\n-600k',8: '60k\n-1,000k', 9:'Above\n 1,000k'}
data['Q8_mapped']=data['Q8'].map(Income_mapping)
sns.countplot(x='Q8_mapped', data=data,ax=axes1[1,1])
axes1[1, 1].set_title('Q8 Family Income')
axes1[1, 1].set_xlabel('Family Income')
axes1[1, 1].set_ylabel('Frequency')
axes1[1, 1].tick_params(axis='x', labelsize=7)
#q9
Hometown_mapping = {3: 'Large cities', 4: 'Medium-sized cities',5: 'Small cities',6:'Towns',7: 'Villages', 8: 'Overseas'}
data['Q9_mapped']=data['Q9'].map(Hometown_mapping)
sns.countplot(x='Q9_mapped', data=data,ax=axes1[1,2])
axes1[1, 2].set_title('Q9 Category of Hometown')
axes1[1, 2].set_xlabel('Hometown')
axes1[1, 2].set_ylabel('Frequency')
axes1[1, 2].tick_params(axis='x', labelsize=7)

#dependent variable
fig, axes2 = plt.subplots(1, 3, figsize=(20, 10))
#q10
PS_mapping = {3: 'Very dissatisfied', 4: 'dissatisfied', 5: 'Neutral', 6: 'Quite satisfied',7: 'Very satisfied'}
data['Q10_mapped']=data['Q10'].map(PS_mapping)
sns.countplot(x='Q10_mapped', data=data,ax=axes2[0])
axes2[0].set_title('Q10 Satisfaction with the current political and social situation',fontsize=8)
axes2[0].set_xlabel('Satisfaction')
axes2[0].set_ylabel('Frequency')
axes2[0].tick_params(axis='x', labelsize=7)
#q11
econ_mapping = {3: 'Very dissatisfied', 4: 'dissatisfied', 5: 'Neutral', 6: 'Quite satisfied',7: 'Very satisfied'}
data['Q11_mapped']=data['Q11'].map(econ_mapping)
sns.countplot(x='Q11_mapped', data=data,ax=axes2[1])
axes2[1].set_title('Q11 Satisfaction with the current economic development situation',fontsize=8)
axes2[1].set_xlabel('Satisfaction')
axes2[1].set_ylabel('Frequency')
axes2[1].tick_params(axis='x', labelsize=7)
#q12
life_mapping = {3: 'Very dissatisfied', 4: 'dissatisfied', 5: 'Neutral', 6: 'Quite satisfied',7: 'Very satisfied'}
data['Q12_mapped']=data['Q12'].map(life_mapping)
sns.countplot(x='Q12_mapped', data=data,ax=axes2[2])
axes2[2].set_title('Q12 Satisfaction with the current  life and work situation',fontsize=8)
axes2[2].set_xlabel('Satisfaction')
axes2[2].set_ylabel('Frequency')
axes2[2].tick_params(axis='x', labelsize=7)

#independent variable
fig, axes3 = plt.subplots(1, 3, figsize=(20, 10))
#q13
interest_mapping = {3: 'not interested \nat all', 4: 'not very \ninterested', 5: 'nuetral', 6: 'quite interested',7: 'very interested'}
data['Q13_mapped']=data['Q13'].map(interest_mapping)
sns.countplot(x='Q13_mapped', data=data,ax=axes3[0])
axes3[0].set_title('Q13 interest in political news',fontsize=8)
axes3[0].set_xlabel('interest')
axes3[0].set_ylabel('Frequency')
axes3[0].tick_params(axis='x', labelsize=7)
#q14
browse_mapping = {3: 'never', 4: '1-2 times \nper month', 5: 'A few times \nper month', 6: 'A few times \nper week',7: ' Almost \nevery day',8:'At least 1 hour \nevery day'}
data['Q14_mapped']=data['Q14'].map(browse_mapping)
sns.countplot(x='Q14_mapped', data=data,ax=axes3[1])
axes3[1].set_title('Q14 How often do you browse current affairs and political news',fontsize=8)
axes3[1].set_xlabel('how often')
axes3[1].set_ylabel('Frequency')
axes3[1].tick_params(axis='x', labelsize=7)
#q15_A8
browse_mapping = {0:'no',1:'yes'}
data['Q15_mapped']=data['Q15_A8'].map(browse_mapping)
sns.countplot(x='Q15_mapped', data=data,ax=axes3[2])
axes3[2].set_title('Q15 Do you browse overseas media and their websites?',fontsize=8)
axes3[2].set_xlabel('Overseas')
axes3[2].set_ylabel('Frequency')
axes3[2].tick_params(axis='x', labelsize=7)
plt.tight_layout()
plt.show()