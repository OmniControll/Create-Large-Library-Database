import yfinance as yf
import pandas as pd
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

# Download historical price data for the stocks
stocks = ['DE', 'GIS', 'MSFT']
start_date = '2014-03-01'
end_date = '2019-03-29'

dfs = []

for stock in stocks:
    data = yf.download(stock, start=start_date, end=end_date, interval='1mo')
    data['Stock'] = stock
    dfs.append(data)

df = pd.concat(dfs)

# Save stock prices to Excel
df.to_excel('stock_prices.xlsx')

# Process the data and compute monthly returns
def calculate_monthly_returns(df):
    df['Monthly_Return'] = df['Adj Close'].pct_change()
    return df

dfs_monthly = []

for stock in stocks:
    stock_data = df[df['Stock'] == stock].copy()
    stock_data = calculate_monthly_returns(stock_data)
    dfs_monthly.append(stock_data)

df_monthly = pd.concat(dfs_monthly)

# Compute mean monthly returns and standard deviations
stats = []

for stock in stocks:
    stock_data = df_monthly[df_monthly['Stock'] == stock]
    mean_return = stock_data['Monthly_Return'].mean()
    std_dev = stock_data['Monthly_Return'].std()
    stats.append([stock, mean_return, std_dev])

stats_df = pd.DataFrame(stats, columns=['Stock', 'Mean_Monthly_Return', 'Standard_Deviation'])

# Calculate the standard deviation of an equally weighted three-stock portfolio
def portfolio_std_dev(stock_correlations, std_devs):
    weights = [1/3, 1/3, 1/3]
    variance = 0

    for i in range(3):
        for j in range(3):
            variance += weights[i] * weights[j] * std_devs[i] * std_devs[j] * stock_correlations.iloc[i, j]

    return sqrt(variance)

stock_correlations = df_monthly.pivot(columns='Stock', values='Monthly_Return').corr()
std_devs = stats_df['Standard_Deviation'].tolist()
portfolio_std_deviation = portfolio_std_dev(stock_correlations, std_devs)

# Save statistics to Excel
stats_df.loc[3] = ['Portfolio', np.mean(stats_df['Mean_Monthly_Return']), portfolio_std_deviation]
stats_df.to_excel('statistics.xlsx', index=False)

# Create an Excel plot with standard deviation (volatility) on the x-axis and average return on the y-axis
x = stats_df['Standard_Deviation']
y = stats_df['Mean_Monthly_Return']
labels = stats_df['Stock']

plt.scatter(x, y)

for i, txt in enumerate(labels):
    plt.annotate(txt, (x[i], y[i]))

plt.xlabel('Standard Deviation (Volatility)')
plt.ylabel('Mean Monthly Return')
plt.title('Risk/Return Profile')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()
