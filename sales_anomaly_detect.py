import pandas as pd
import numpy as np

# 1️⃣ Load cleaned data
data = pd.read_csv('sales_history_clean.csv')
data['date'] = pd.to_datetime(data['date'])

# 2️⃣ Aggregate total sales per day
daily_sales = data.groupby('date')['total_sales'].sum().reset_index()

# 3️⃣ Calculate mean and std
mean_sales = daily_sales['total_sales'].mean()
std_sales = daily_sales['total_sales'].std()

# 4️⃣ Calculate Z-score
daily_sales['z_score'] = (daily_sales['total_sales'] - mean_sales) / std_sales

# 5️⃣ Mark anomalies (Z-score > 2 or < -2)
daily_sales['anomaly'] = daily_sales['z_score'].apply(lambda x: 'Yes' if abs(x) > 2 else 'No')

# 6️⃣ Show anomalies
anomalies = daily_sales[daily_sales['anomaly'] == 'Yes']
print("Anomalies detected:")
print(anomalies)

# 7️⃣ Save anomalies CSV
daily_sales.to_csv('daily_sales_anomalies.csv', index=False)
print("Daily sales with anomalies saved as 'daily_sales_anomalies.csv'")
