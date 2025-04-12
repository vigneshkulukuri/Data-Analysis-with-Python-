import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")

category_returns = df.groupby("Product Category")['Returns'].sum()

# Create Pie Chart
plt.figure(figsize=(8,6))
colors = sns.color_palette('pastel')  # Using Seaborn's color palette

plt.pie(category_returns, labels=category_returns.index, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title("Total Returns by Product Category")
plt.show()
