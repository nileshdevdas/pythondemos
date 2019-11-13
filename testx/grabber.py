import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.google.com')
theHtml = data.text
print(theHtml)
# this is a searchable tree
parsedHTMLTree=  BeautifulSoup(theHtml, features='lxml')
print(parsedHTMLTree.title)
print(parsedHTMLTree.find("div", {'id': 'logo-default'}))
#<html><div id="price">1212323</div></html>
