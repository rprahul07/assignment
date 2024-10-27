import pandas as pd
import numpy as np
import psycopg2

# Connecting to PostgreSQL database
# Replacing 'your_db', 'your_user', 'your_password' with your database credentials
conn = psycopg2.connect("dbname='stock_database' user='rprahul' password='Rahul@123' host='localhost'")

# Loading data from the table 'hindalco_data' into a DataFrame
data = pd.read_sql('SELECT * FROM stock_data', conn)
conn.close()  # Close the connection

# Calculating 20-day and 50-day simple moving averages (SMA) for the 'close' price
data['SMA_20'] = data['close'].rolling(window=20).mean()
data['SMA_50'] = data['close'].rolling(window=50).mean()

# 1 when SMA_20 is greater than SMA_50, 0 otherwise
data['Signal'] = 0  # Initialize signal column to 0
data.loc[20:, 'Signal'] = np.where(data['SMA_20'][20:] > data['SMA_50'][20:], 1, 0)

# Calculating the position 
data['Position'] = data['Signal'].diff()

# Calculating daily returns of the stock
data['Returns'] = data['close'].pct_change()

# Calculating strategy returns by multiplying daily returns with previous day's signal
data['Strategy_Returns'] = data['Returns'] * data['Signal'].shift(1)

# Calculate  returns for both strategy and market
cumulative_strategy_returns = (1 + data['Strategy_Returns']).cumprod() - 1
cumulative_market_returns = (1 + data['Returns']).cumprod() - 1

# Display cumulative returns
print("Cumulative Strategy Returns:", cumulative_strategy_returns.iloc[-1])
print("Cumulative Market Returns:", cumulative_market_returns.iloc[-1])
