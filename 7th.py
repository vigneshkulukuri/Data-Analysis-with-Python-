import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")
df = pd.read_csv(r"D:\Python Project\ecommerce_customer_data_custom_ratios.csv")
df["Total Purchase Amount"] = pd.to_numeric(df["Total Purchase Amount"], errors='coerce')

# Identify top 5 product categories by total sales
top_categories = df.groupby('Product Category')['Total Purchase Amount'].sum().nlargest(5).index

# Filter dataset to include only these categories
df = df[df['Product Category'].isin(top_categories)]

# Box Plot: Distribution of Total Purchase Amount for Top 5 Product Categories
plt.figure(figsize=(8, 6))
sns.boxplot(x='Product Category', y='Total Purchase Amount', data=df, hue='Product Category', palette="viridis", legend=False)
plt.xlabel("Product Category")
plt.ylabel("Total Purchase Amount")
plt.title("Box Plot: Total Purchase Amount by Top 5 Product Categories")
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.show()