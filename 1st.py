import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"V:\ecommerce_customer_data_custom_ratios.csv")
# Convert 'Purchase Date' to datetime format
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
# Extract year and month
df['Month'] = df['Purchase Date'].dt.strftime('%Y-%m')

# Calculate total sales per month
monthly_sales = df.groupby('Month')['Total Purchase Amount'].sum()

# Plot monthly sales trend
plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='*', linestyle='-', color='b')

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.grid()

plt.show()
