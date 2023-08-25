import requests
from bs4 import BeautifulSoup

URL = "https://www.sneakernews.com"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the div containing the sneaker release information
sneaker_div = soup.find(class_="sneaker-release-calendar")

# Find all of the sneaker release rows
sneaker_rows = sneaker_div.find_all(class_="sneaker-release-row")

# Loop through each row and print the sneaker name and release date
for row in sneaker_rows:
    name_div = row.find(class_="sneaker-name")
    release_div = row.find(class_="release-date")

    name = name_div.text.strip()
    release_date = release_div.text.strip()

    print(f"{name}: {release_date}")
