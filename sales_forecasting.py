import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# 1️⃣ Load cleaned data
data = pd.read_csv('sales_history_clean.csv')
data['date'] = pd.to_datetime(data['date'])

# 2️⃣ Prepare data for Prophet
df = data.groupby('date')['total_sales'].sum().reset_index()
df = df.rename(columns={'date':'ds', 'total_sales':'y'})  # Prophet needs ds & y columns

# 3️⃣ Create and fit model
model = Prophet()
model.fit(df)

# 4️⃣ Forecast next 90 days (approx 3 months)
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# 5️⃣ Plot forecast
fig1 = model.plot(forecast)
plt.title("Sales Forecast (Next 3 Months)")
plt.savefig('sales_forecast.png')
plt.close()

print("Forecast created! Check 'sales_forecast.png'.")
