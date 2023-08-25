import pandas as pd
import openpyxl
import yfinance as yf
import time

while True:
    # Scrape the data
    data = yf.Ticker("BTC-USD").history()

    # Load the existing Excel workbook and add a sheet to it
    workbook = openpyxl.load_workbook("sneakers1.xlsx")
    sheet = workbook.active

    # Add the data to the sheet
    for i, row in data.iterrows():
        sheet.append(row)

    # Save the workbook
    workbook.save("sneakers1.xlsx")

    # Wait 24 hours before scraping the data again
    time.sleep(24 * 3600)
