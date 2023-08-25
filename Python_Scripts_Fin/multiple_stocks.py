import yfinance as yf
import pandas as pd
import datetime

# Set the ticker symbols for the cryptocurrencies and stocks
crypto_tickers = ["BTC-USD", "ETH-USD"]
stock_tickers = ["MSFT", "TSLA", "COIN", "GOOGL", "NVDA", "ASML"]

# Get the current date and subtract three years to get the start date
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365*3)

# Create empty dictionaries to store the data
crypto_data = {}
stock_data = {}

# Loop through the crypto ticker symbols
for ticker in crypto_tickers:
    # Get the stock data for the ticker
    data = yf.Ticker(ticker).history(start=start_date, end=end_date)
    
    # Fill the NaN values with the forward-fill strategy
    data = data.fillna(method='ffill')
    
    # Select the "Close" column and resample the data to get the mean close price per month
    monthly_data = data["Close"].resample("M").mean()
    
    # Round the values to 2 decimal places
    monthly_data = monthly_data.round(2)
    
    # Remove the time component from the date index
    monthly_data.index = monthly_data.index.normalize()
    
    # Add the resampled data to the dictionary
    crypto_data[ticker] = monthly_data

# Do the same for the stock ticker symbols
for ticker in stock_tickers:
    data = yf.Ticker(ticker).history(start=start_date, end=end_date)
    data = data.fillna(method='ffill')
    monthly_data = data["Close"].resample("M").mean()
    monthly_data = monthly_data.round(2)
    monthly_data.index = monthly_data.index.normalize()
    stock_data[ticker] = monthly_data

# Convert the dictionaries to DataFrames
crypto_df = pd.DataFrame(crypto_data)
stock_df = pd.DataFrame(stock_data)

# Merge the two dataframes on the Date index
df = pd.merge(crypto_df, stock_df, left_index=True, right_index=True, how='outer')

# Convert the DataFrame to a CSV file
df.to_csv('data2.csv')

# Print the data
print(df)
