from bs4 import BeautifulSoup
import urllib.request
import json
import requests

def getSnow():
    #手稲スキー場のゲレンデレポートのページ
    url = 'https://sapporo-teine.com/snow/gelande-report'
    #HTTPリクエスト
    r = requests.get(url)

    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
    snow = soup.find_all("dd",{"class": "greport__data__content"})

    print("【手稲スキー場】")
    print("24時間積雪量:" + snow[0].text)
    print("山頂の総積雪量:" + snow[1].text)
    print("山麓の総積雪量:" + snow[2].text)
    print("雪質:" + snow[3].text)

    return snow

getSnow()    

# tags = soup.find_all("dd",{"class": "greport__data__content"})

#print(tags)