import pandas as pd

df = pd.read_excel("raw-data-I.xlsx")
threshold = 12.16
filtered_values = df[df.iloc[:, 0] < threshold].iloc[:, 0]
mean_value = filtered_values.mean()
print("Mean of filtered values:", mean_value)