import requests
page = requests.get("https://progameguides.com/borderlands/borderlands-3-shift-codes-list-guide/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
