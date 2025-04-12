import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")
df = pd.read_csv(r"D:\Python Project\ecommerce_customer_data_custom_ratios.csv")
# Summarize total purchase amount by payment method and product category
purchase_summary = df.groupby(["Payment Method", "Product Category"])["Total Purchase Amount"].sum().reset_index()

# Plot using a line plot
plt.figure(figsize=(8, 6))
sns.lineplot(data=purchase_summary, x="Payment Method", y="Total Purchase Amount", hue="Product Category", marker="o", linewidth=2)

# Labels and title
plt.xlabel("Payment Method")
plt.ylabel("Total Purchase Amount")
plt.title("Total Purchase Amount by Payment Method and Product Category")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend(title="Product Category")

# Show plot
plt.show()