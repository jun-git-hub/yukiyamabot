from bs4 import BeautifulSoup
import requests
import json

def getSnow():

    #ブラウザによる違いをなくすための合言葉
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '\
         'AppleWebKit/537.36 (KHTML, like Gecko) '\
         'Chrome/67.0.3396.99 Safari/537.36 '

    #手稲スキー場のゲレンデレポートのページ
    url_teine = 'https://sapporo-teine.com/snow/gelande-report'
    
    #HTTPリクエスト
    html_teine = requests.get(url_teine)
    html_doc_teine = requests.get(url_teine).text

    #htmlの解析
    soup_teine = BeautifulSoup(html_teine.content, 'html.parser') 
    
    snow_teine = soup_teine.find_all("dd",{"class": "greport__data__content"})

    title_teine = "【手稲スキー場】"
    sekisetsu_teine = "24時間積雪量:" + snow_teine[0].text
    sancho_teine = "山頂の総積雪量:" + snow_teine[1].text
    fumoto_teine = "山麓の総積雪量:" + snow_teine[2].text
    yukishitsu_teine = "雪質:" + snow_teine[3].text

    teine_result = title_teine + "\n" + sekisetsu_teine + "\n" + sancho_teine + "\n" + fumoto_teine + "\n" + yukishitsu_teine
#---------------------------------
    #ルスツスキー場のゲレンデレポートのページ
    url_rusutsu = 'https://rusutsu.com/snow-and-weather-report/'
    
    #HTTPリクエスト
    html_rusutsu = requests.get(url_rusutsu)
    html_doc_rusutsu = requests.get(url_rusutsu).text

    #htmlの解析
    soup_rusutsu = BeautifulSoup(html_rusutsu.content, 'html.parser') 

    snow_rusutsu = soup_rusutsu.find_all("li",{"class": "status02"})

    title_rusutsu = "【ルスツスキー場】"
    sekisetsu_rusutsu = snow_rusutsu[0].contents[3].text
    total_sekisetsu_rusutsu = snow_rusutsu[0].contents[1].text
    yukishitsu_rusutsu = snow_rusutsu[0].contents[5].text

    rusutsu_result = title_rusutsu + "\n" + sekisetsu_rusutsu + "\n" + total_sekisetsu_rusutsu + "\n" + yukishitsu_rusutsu
    
    return teine_result + "\n---------------\n" + rusutsu_result





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