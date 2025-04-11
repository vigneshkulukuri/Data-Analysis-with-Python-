import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")

plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=20, color="blue", kde=True)  # KDE adds the trend line
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Customers with Trend Line")
plt.grid(axis="y")
plt.show()