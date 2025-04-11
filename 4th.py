import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")
category_gender_counts = df.groupby(["Product Category", "Gender"]).size().reset_index(name="Count")

# Plot using a grouped bar chart
plt.figure(figsize=(14, 7))
sns.barplot(data=category_gender_counts, x="Product Category", y="Count", hue="Gender", palette="Paired", edgecolor="black")

plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Number of Purchases", fontsize=12)
plt.title("Product Category Preference by Gender", fontsize=14, fontweight="bold")
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title="Gender", fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()