import requests

# Replace YOUR-API-KEY with your actual API key
API_KEY = "YOUR-API-KEY"

# Specify the cryptocurrency symbol (e.g. BTC for Bitcoin)
symbol = "BTC"

# Make the API request
URL = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
headers = {"X-CMC_PRO_API_KEY": API_KEY}
response = requests.get(URL, headers=headers)

# Extract the price data from the response
data = response.json()
price_data = data["data"][symbol]["quote"]["USD"]

# Print the price data
print(f"Price: {price_data['price']}")
print(f"Volume (24h): {price_data['volume_24h']}")
print(f"Market cap: {price_data['market_cap']}")
