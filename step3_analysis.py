import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import numpy as np

# ----------------------------
# 1️⃣ Load cleaned data
# ----------------------------
data = pd.read_csv('sales_history_clean.csv')
data['date'] = pd.to_datetime(data['date'])

# ----------------------------
# 2️⃣ Forecasting (Next 90 days)
# ----------------------------
df_forecast = data.groupby('date')['total_sales'].sum().reset_index()
df_forecast = df_forecast.rename(columns={'date':'ds','total_sales':'y'})

model = Prophet()
model.fit(df_forecast)

future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# Save forecast plot
fig1 = model.plot(forecast)
plt.title("Sales Forecast (Next 3 Months)")
plt.savefig('sales_forecast.png')
plt.close()

# ----------------------------
# 3️⃣ KPI Anomaly Detection
# ----------------------------
daily_sales = df_forecast.copy()
mean_sales = daily_sales['y'].mean()
std_sales = daily_sales['y'].std()

daily_sales['z_score'] = (daily_sales['y'] - mean_sales)/std_sales
daily_sales['anomaly'] = daily_sales['z_score'].apply(lambda x: 'Yes' if abs(x)>2 else 'No')

# Save anomalies CSV
daily_sales.to_csv('daily_sales_anomalies.csv', index=False)

# ----------------------------
# 4️⃣ Charts: Easy Visuals
# ----------------------------
# Total sales over time
plt.figure(figsize=(10,5))
daily_sales.plot(x='ds', y='y', kind='line', marker='o', title='Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.savefig('total_sales_over_time.png')
plt.close()

# Sales by region
plt.figure(figsize=(8,5))
region_sales = data.groupby('region')['total_sales'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', color='skyblue', title='Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.savefig('sales_by_region.png')
plt.close()

# Sales by product
plt.figure(figsize=(8,5))
product_sales = data.groupby('product')['total_sales'].sum().sort_values(ascending=False)
product_sales.plot(kind='bar', color='orange', title='Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.savefig('sales_by_product.png')
plt.close()

print("✅ Step 3 Complete! Check PNG images & daily_sales_anomalies.csv")
