import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('multiple.xlsx', sheet_name='RNA')

# 根据'label'列进行分组，并计算每组的标准差
std_series = df.groupby('Label')['DDG'].std()

# 将标准差映射回原始DataFrame，如果没有重复值则将标准差设为0
df['std'] = df['Label'].map(std_series).fillna(0)

# 保存修改后的DataFrame到新的 Excel 文件
df.to_excel('RNA_std.xlsx', index=False)
