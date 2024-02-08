#// pip3 install requests
import requests

#// pip3 install beautifulsoup4
from bs4 import BeautifulSoup
#https://www.youtube.com/watch?v=MH3641s3Roc&t=1131s
#site for scrapping ::https://books.toscrape.com/catalogue/page-1.html
#// pip3 install pandas
import pandas as pd

books = []

for i in range(1,5):
  url = f"https://books.toscrape.com/catalogue/page-{i}.html"
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  #ol = soup.find('ol')
  #articles = ol.find_all('article', class_='product_pod')
  articles = soup.find_all('article', class_='product_pod')
  for article in articles:
    title=article.find('img').attrs['alt']
    star = article.find('p')['class'][1]
    price = article.find('p', class_='price_color').text
    price = float(price[1:])
    books.append([title, star, price])


df = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price'])
df