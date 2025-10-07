import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt


data = pd.read_csv('sales_history_clean.csv')
data['date'] = pd.to_datetime(data['date'])

df = data.groupby('date')['total_sales'].sum().reset_index()
df = df.rename(columns={'date':'ds', 'total_sales':'y'}) 


model = Prophet()
model.fit(df)


future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)


fig1 = model.plot(forecast)
plt.title("Sales Forecast (Next 3 Months)")
plt.savefig('sales_forecast.png')
plt.close()

print("Forecast created! Check 'sales_forecast.png'.")
