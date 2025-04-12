import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")
df = pd.read_csv(r"D:\Python Project\ecommerce_customer_data_custom_ratios.csv")
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

# Aggregate total sales by purchase date
df_grouped = df.groupby('Purchase Date')['Total Purchase Amount'].sum()

# Scatter Plot: Purchase Date vs. Total Purchase Amount
plt.figure(figsize=(8, 6))
plt.scatter(df_grouped.index, df_grouped.values, color='red', s=50, alpha=0.7)

plt.xlabel("Purchase Date")
plt.ylabel("Total Purchase Amount")
plt.title("Scatter Plot: Total Purchase Amount Over Time")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()