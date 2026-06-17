import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('RNA.xlsx', sheet_name='Sheet1')

# 统计每个label的出现次数
label_counts = df['Label'].value_counts()

# 将统计结果添加到 DataFrame 中
df['label_count'] = df['Label'].map(label_counts)

# 将结果保存到新的 Excel 文件
df.to_excel('RNA_C.xlsx', index=False)
