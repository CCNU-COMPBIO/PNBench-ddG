import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('RNA.xlsx', sheet_name='Sheet1')

# 根据'label'列进行分组，并计算每组的标准差和平均值
grouped = df.groupby('Label')['DDG']
std_series = grouped.std()
mean_series = grouped.mean()

# 将标准差映射回原始DataFrame，如果没有重复值则将标准差设为0
df['std'] = df['Label'].map(std_series).fillna(0)
# 将平均值映射回原始DataFrame，如果没有重复值则将平均值设为0
df['mean'] = df['Label'].map(mean_series).fillna(0)

# 保存修改后的DataFrame到新的 Excel 文件
df.to_excel('RNA_MEAN.xlsx', index=False)
