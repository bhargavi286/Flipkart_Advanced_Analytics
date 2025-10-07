import pandas as pd

# CSV file open cheyyi
data = pd.read_csv('sales_history.csv')

# total_sales column calculate cheyyi
data['total_sales'] = data['units_sold'] * data['unit_price']  # correct column name

# Check first 5 rows
print(data.head())

# Save updated CSV
data.to_csv('sales_history_clean.csv', index=False)
