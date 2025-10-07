import pandas as pd
import numpy as np


data = pd.read_csv('sales_history_clean.csv')
data['date'] = pd.to_datetime(data['date'])


daily_sales = data.groupby('date')['total_sales'].sum().reset_index()


mean_sales = daily_sales['total_sales'].mean()
std_sales = daily_sales['total_sales'].std()


daily_sales['z_score'] = (daily_sales['total_sales'] - mean_sales) / std_sales


daily_sales['anomaly'] = daily_sales['z_score'].apply(lambda x: 'Yes' if abs(x) > 2 else 'No')


anomalies = daily_sales[daily_sales['anomaly'] == 'Yes']
print("Anomalies detected:")
print(anomalies)


daily_sales.to_csv('daily_sales_anomalies.csv', index=False)
print("Daily sales with anomalies saved as 'daily_sales_anomalies.csv'")
