import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")
df = pd.read_csv(r"D:\Python Project\ecommerce_customer_data_custom_ratios.csv")
numeric_df = df.select_dtypes(include=['number'])
# Compute correlation matrix
correlation_matrix = numeric_df.corr()
# Heatmap: Correlation Between Variables
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5) 
plt.title("Correlation Heatmap")
plt.show()