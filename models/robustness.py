import pandas as pd
import statsmodels.api as sm
data = pd.read_csv('/Users/zhengchuyi/Desktop/the-impact-of-news-information-acquisition-and-cognition/data/processed/processed_data.csv')
print(data.head())
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
pol_sat_model_1 = sm.OLS(pol_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown], axis=1))).fit()
pol_sat_model_2 = sm.OLS(pol_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest], axis=1))).fit()
pol_sat_model_3 = sm.OLS(pol_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time], axis=1))).fit()
pol_sat_model_4 = sm.OLS(pol_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time, overseas], axis=1))).fit()

eco_sati_model_1 = sm.OLS(eco_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown], axis=1))).fit()
eco_sati_model_2 = sm.OLS(eco_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest], axis=1))).fit()
eco_sati_model_3 = sm.OLS(eco_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time], axis=1))).fit()
eco_sati_model_4 = sm.OLS(eco_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time, overseas], axis=1))).fit()

lif_work_sati_model_1 = sm.OLS(lif_work_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown], axis=1))).fit()
lif_work_sati_model_2 = sm.OLS(lif_work_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest], axis=1))).fit()
lif_work_sati_model_3 = sm.OLS(lif_work_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time], axis=1))).fit()
lif_work_sati_model_4 = sm.OLS(lif_work_sati, sm.add_constant(pd.concat([gender, poli_afli, gra_uni, hig_maj, ann_inc, hometown, interest, time, overseas], axis=1))).fit()

print("Pol Sati Model 1:")
print(pol_sat_model_1.summary())

print("\nPol Sati Model 2:")
print(pol_sat_model_2.summary())

print("\nPol Sati Model 3:")
print(pol_sat_model_3.summary())

print("\nPol Sati Model 4:")
print(pol_sat_model_4.summary())

print("\nEco Sati Model 1:")
print(eco_sati_model_1.summary())

print("\nEco Sati Model 2:")
print(eco_sati_model_2.summary())

print("\nEco Sati Model 3:")
print(eco_sati_model_3.summary())

print("\nEco Sati Model 4:")
print(eco_sati_model_4.summary())

print("\nLif Work Sati Model 1:")
print(lif_work_sati_model_1.summary())

print("\nLif Work Sati Model 2:")
print(lif_work_sati_model_2.summary())

print("\nLif Work Sati Model 3:")
print(lif_work_sati_model_3.summary())

print("\nLif Work Sati Model 4:")
print(lif_work_sati_model_4.summary())

import pandas as pd
import statsmodels.api as sm

# 读取数据
data = pd.read_csv(
    '/Users/zhengchuyi/Desktop/the-impact-of-news-information-acquisition-and-cognition/data/processed/processed_data.csv')

# 定义因变量和模型名称的映射关系
dependent_variables = ['Q10', 'Q11', 'Q12']
model_names = ['model_1', 'model_2', 'model_3', 'model_4']

# 创建一个空的 DataFrame 用于存储所有模型结果
result_dfs = []

# 遍历每个因变量
for dependent_variable in dependent_variables:
    # 创建一个空的 DataFrame 用于存储当前因变量的所有模型结果
    result_df_temp = pd.DataFrame()

    # 遍历每个模型
    for model_name in model_names:
        # 构建自变量列表，注意替换为你实际使用的列名
        independent_variables = ['Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']
        if model_name in ['model_2', 'model_3', 'model_4']:
            independent_variables.append('Q10')
        if model_name in ['model_3', 'model_4']:
            independent_variables.append('Q11')
        if model_name == 'model_4':
            independent_variables.append('Q12')

        # 构建模型
        model = sm.OLS(data[dependent_variable], sm.add_constant(data[independent_variables])).fit()

        # 提取关键结果
        summary_data = {
            'Model': model_name,
            'R-squared': model.rsquared,
            'Coefficients': model.params,
            # 其他需要的关键结果
        }

        # 将结果添加到当前模型的结果表
        result_df_temp = pd.concat([result_df_temp, pd.DataFrame([summary_data])], ignore_index=True)

    # 将当前因变量的结果表添加到结果列表
    result_dfs.append((dependent_variable, result_df_temp))

# 打印或保存结果
for dependent_variable, result_df_temp in result_dfs:
    print(f"\nResults for Dependent Variable: {dependent_variable}")
    print(result_df_temp)
    # 如果需要保存到文件，可以使用 result_df_temp.to_csv() 或 result_df_temp.to_excel() 等方法



import pandas as pd
from tabulate import tabulate

# 创建一个空的 DataFrame 用于存储所有模型结果
result_df = pd.DataFrame()

from tabulate import tabulate

# 遍历每个因变量
for dependent_variable, result_df_temp in result_dfs:
    # 打印或保存当前因变量的结果表
    print(f"\nResults for Dependent Variable: {dependent_variable}")
    print(tabulate(result_df_temp, headers='keys', tablefmt='pretty'))


