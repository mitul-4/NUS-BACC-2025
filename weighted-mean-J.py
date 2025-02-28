import pandas as pd

df = pd.read_excel("raw-data-J.xlsx")

threshold = 5

filtered_values_1 = df[df.iloc[:, 0] < threshold].iloc[:, 0]
mean_value_1 = filtered_values_1.mean()
print("mean of filtered values 1:", mean_value_1)

filtered_values_2 = df[df.iloc[:, 0] > threshold].iloc[:, 0]
mean_value_2 = filtered_values_2.mean()
print("mean of filtered values 2:", mean_value_2)

# weighted_mean = (mean_value_1 * len(filtered_values_1) + mean_value_2 * len(filtered_values_2)) / (len(filtered_values_1) + len(filtered_values_2))
weighted_mean = (mean_value_1 * 0.7) + (mean_value_2 * 0.3)
print("weighted mean:", weighted_mean)