from bs4 import BeautifulSoup
import requests
import json
import requests

def getSnow():
    #手稲スキー場のゲレンデレポートのページ
    url = 'https://sapporo-teine.com/snow/gelande-report'

    #ブラウザによる違いをなくすための合言葉
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '\
         'AppleWebKit/537.36 (KHTML, like Gecko) '\
         'Chrome/67.0.3396.99 Safari/537.36 '
    
    #HTTPリクエスト
    html = requests.get(url)
    html_doc = requests.get(url).text

    #htmlの解析
    soup = BeautifulSoup(html.content, 'html.parser') 
    
    snow = soup.find_all("dd",{"class": "greport__data__content"})

    title = "【手稲スキー場】"
    sekisetsu = "24時間積雪量:" + snow[0].text
    sancho = "山頂の総積雪量:" + snow[1].text
    fumoto = "山麓の総積雪量:" + snow[2].text
    yukishitsu = "雪質:" + snow[3].text

    print(title + "\n" + sekisetsu + "\n" + sancho + "\n" + fumoto + "\n" + yukishitsu)

getSnow()

#ライブラリのインポート
#import requests
#from bs4 import BeautifulSoup
#import urllib.request
#import json


#def getWeather():
    #tenki.jpの目的の地域のページのURL（今回は東京都調布市）
#    url = 'https://tenki.jp/forecast/3/16/4410/13208/'
    #HTTPリクエスト
#    r = requests.get(url)

    #HTMLの解析
 #   bsObj = BeautifulSoup(r.content, "html.parser")

    #今日の天気を取得
 #   today = bsObj.find(class_="today-weather")
 #   weather = today.p.string

    #気温情報のまとまり
 #   temp=today.div.find(class_="date-value-wrap")

    #気温の取得
 #   temp=temp.find_all("dd")
 #   temp_max = temp[0].span.string #最高気温
 #   temp_max_diff=temp[1].string #最高気温の前日比
 #   temp_min = temp[2].span.string #最低気温
 #   temp_min_diff=temp[3].string #最低気温の前日比

    #とりあえず動くのを見たいので天気と気温を繋げて返しています。
 #   return weather+temp_max+temp_min