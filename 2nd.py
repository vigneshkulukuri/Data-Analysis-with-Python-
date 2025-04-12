
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")


plt.figure(figsize=(12,6))
sns.histplot(data=df, x="Customer Age", hue="Payment Method", multiple="stack", bins=20, palette="Set2")

plt.xlabel("Customer Age")
plt.ylabel("Count")
plt.title("Distribution of Customer Age by Payment Method")
plt.legend("Payment Method")  # Corrected

plt.show()
