import pandas as pd


data = pd.read_csv('sales_history.csv')


data['total_sales'] = data['units_sold'] * data['unit_price']

print(data.head())


data.to_csv('sales_history_clean.csv', index=False)
