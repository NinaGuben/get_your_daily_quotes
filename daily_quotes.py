import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup_object = BeautifulSoup(response.text, "html.parser")
quotes = soup_object.find_all("div", class_ = "quote")
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print("quote:", text)
    print("euthor:", author)
    print("........................")