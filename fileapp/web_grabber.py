from bs4 import BeautifulSoup
import requests

htmlPage = requests.get(
    "https://www.flipkart.com/casio-wk-7600-kh30-digital-portable-keyboard/p/itmfftfwykqjgh54")
parsedTree = BeautifulSoup(htmlPage.text, features='lxml')
print(parsedTree.title.text)
print(parsedTree.find("div", {'class': '_1vC4OE _3qQ9m1'}).text)


amazonPage = requests.get(
    "https://www.amazon.in/Casio-WK7600-76-Key-Workstation-Keyboard/dp/B00GXNS5PU/ref=sr_1_1?crid=1QRU86WM1PE17&keywords=wk7600&qid=1573556061&sprefix=wk7600%2Caps%2C419&sr=8-1",
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'})
amazon_parsed_tree = BeautifulSoup(amazonPage.text, features='lxml')
print(amazon_parsed_tree.find("span", {'id': 'priceblock_ourprice'}).text)
