import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")
df = pd.read_csv(r"D:\Python Project\ecommerce_customer_data_custom_ratios.csv")
bins = [18, 25, 35, 45, 55, 65, 100]  # Age ranges
labels = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]

# Create Age Group column
df["Age Group"] = pd.cut(df["Customer Age"], bins=bins, labels=labels, right=False)

# Count purchases per product category by age group (explicitly setting observed=False)
category_age_counts = df.groupby(["Product Category", "Age Group"], observed=False).size().unstack()

# Plot
plt.figure(figsize=(8, 6))
category_age_counts.plot(kind="bar", figsize=(14, 7), colormap="viridis")

plt.xlabel("Product Category")
plt.ylabel("Number of Purchases")
plt.title("Product Category Preference by Age Group")
plt.xticks(rotation=45)
plt.legend(title="Age Group")
plt.show()