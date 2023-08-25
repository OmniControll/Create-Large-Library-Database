import webbrowser

# Set of websites to open
websites = [
    "https://www.google.com",
    "https://www.tradingview.com/chart/THEnTgEw/?symbol=COINBASE%3ABTCEUR",
    "https://chat.openai.com/chat",
    "https://brightspace.hhs.nl/d2l/home"
]

# Open the websites in new tabs
for website in websites:
    webbrowser.open_new_tab(website)
