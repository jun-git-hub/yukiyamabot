from bs4 import BeautifulSoup
import requests

def getSnow():

    #ブラウザによる違いをなくすための合言葉
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '\
         'AppleWebKit/537.36 (KHTML, like Gecko) '\
         'Chrome/67.0.3396.99 Safari/537.36 '

    #ルスツスキー場のゲレンデレポートのページ
    url_rusutsu = 'https://rusutsu.com/snow-and-weather-report/'
    
    #HTTPリクエスト
    html_rusutsu = requests.get(url_rusutsu)
    html_doc_rusutsu = requests.get(url_rusutsu).text

    #htmlの解析
    soup_rusutsu = BeautifulSoup(html_rusutsu.content, 'html.parser') 

    #スクレイピング
    snow_rusutsu = soup_rusutsu.find_all("li",{"class": "status02"})

    #降雪量等を抽出
    title_rusutsu = "【ルスツスキー場】"
    sekisetsu_rusutsu = snow_rusutsu[0].contents[3].text
    total_sekisetsu_rusutsu = snow_rusutsu[0].contents[1].text
    yukishitsu_rusutsu = snow_rusutsu[0].contents[5].text

    rusutsu_result = title_rusutsu + "\n" + sekisetsu_rusutsu + "\n" + total_sekisetsu_rusutsu + "\n" + yukishitsu_rusutsu
    
    return rusutsu_result





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