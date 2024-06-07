from bs4 import BeautifulSoup
import urllib.request

url =  'https://vnexpress.net/giao-duc'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
list_article = soup.find_all('article',class_='item-news item-news-common')
for data in list_article:
	x = data.find("a")
	print(x["title"])
	print(x["href"])