main_title: Python Scraping Cheatsheet
lang: python
#------------------------------------------------------------------------------
title: requests + BeautifulSoup
from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.independent.co.uk/arts-entertainment/books/features/best-kids-books-ever-list-b2207921.html'
page = requests.get(url);
soup = BeautifulSoup(page.content, "html.parser")
strongs = soup.select('p strong')
titles = [ s.text for s in strongs if re.match('\d{1,2}\.', s.text.strip()) ]

#------------------------------------------------------------------------------
title: helium + BeautifulSoup
browser = start_chrome("https://www.abcbourse.com/marches/aaz?M=sp500u", headless=False)
html = browser.page_source
click("Tout accepter et continuer")
soup = BeautifulSoup(html, 'html.parser')
trs = soup.find_all('tr', class_='alri')
for r in parse_table(trs):
   results.append(r)
#------------------------------------------------------------------------------
