from bs4 import BeautifulSoup
import urllib.request
import json
import requests

url = 'https://sapporo-teine.com/snow/gelande-report'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/67.0.3396.99 Safari/537.36 '

html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化

print("手稲スキー場の")
print("24時間積雪量")
print("山頂の総積雪量")
print("山麓の総積雪量")
print("雪質")
print("----------------")

for element in soup.find_all("dd",{"class": "greport__data__content"}):
    print(element.text)

# tags = soup.find_all("dd",{"class": "greport__data__content"})

#print(tags)