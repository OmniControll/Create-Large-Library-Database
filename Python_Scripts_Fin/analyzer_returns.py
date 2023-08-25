import yfinance as yf
import pyfolio as pf

# Get the stock data for BTC-USD
data = yf.Ticker("BTC-USD").history()

# Resample the data to monthly intervals and calculate the mean close price
monthly_data = data["Close"].resample("M").mean()

# Calculate the monthly returns
returns = monthly_data.pct_change()

# Get the number of observations in the data
num_obs = len(returns)

# Set the number of returns to 24 or the number of observations, whichever is smaller
num_returns = min(12, num_obs)

# Select the last num_returns months of data
returns = returns.tail(num_returns)

# Analyze the returns and generate a full tear sheet report
pf.create_full_tear_sheet(returns)
