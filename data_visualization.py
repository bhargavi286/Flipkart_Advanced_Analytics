import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('sales_history_clean.csv')
data['date'] = pd.to_datetime(data['date'])


plt.figure(figsize=(10,5))
data.groupby('date')['total_sales'].sum().plot(kind='line', marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.savefig('total_sales_over_time.png')  # Save only
plt.close()

plt.figure(figsize=(8,5))
data.groupby('region')['total_sales'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.savefig('sales_by_region.png')
plt.close()


plt.figure(figsize=(8,5))
data.groupby('product')['total_sales'].sum().sort_values(ascending=False).plot(kind='bar', color='orange')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.savefig('sales_by_product.png')
plt.close()

print("Charts created successfully! Check PNG files in the same folder.")
