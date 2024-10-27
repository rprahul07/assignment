import pandas as pd
import psycopg2

# Loading data from the CSV
data = pd.read_csv("https://docs.google.com/spreadsheets/d/1-rIkEb94tZ69FvsjXnfkVETYu6rftF-8/export?format=csv")

# Connecting to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="stock_database",
    user="rprahul",
    password="Rahul@123"
)
cur = conn.cursor()

# Creating table if it does not exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS stock_data (
        id SERIAL PRIMARY KEY,
        instrument VARCHAR(255),
        datetime TIMESTAMP,
        open DECIMAL(10, 2),
        high DECIMAL(10, 2),
        low DECIMAL(10, 2),
        close DECIMAL(10, 2),
        volume INTEGER
    );
""")

# Inserting data into the table
for index, row in data.iterrows():
    cur.execute("""
        INSERT INTO stock_data (instrument, datetime, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (row['instrument'], row['datetime'], row['open'], row['high'], row['low'], row['close'], row['volume']))

# Commiting changes and close connection
conn.commit()

cur.close()

conn.close()

print("Data loaded successfully!")  