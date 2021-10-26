from bs4 import BeautifulSoup
import requests

def getSnow_teine():

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

    return teine_result
#---------------------------------
def getSnow_rusutsu():

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

    snow_rusutsu = soup_rusutsu.find_all("li",{"class": "status02"})

    title_rusutsu = "【ルスツスキー場】"
    sekisetsu_rusutsu = snow_rusutsu[0].contents[3].text
    total_sekisetsu_rusutsu = snow_rusutsu[0].contents[1].text
    yukishitsu_rusutsu = snow_rusutsu[0].contents[5].text

    rusutsu_result = title_rusutsu + "\n" + sekisetsu_rusutsu + "\n" + total_sekisetsu_rusutsu + "\n" + yukishitsu_rusutsu
    
    return rusutsu_result

#---------------------------------
def getSnow_Kokusai():

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

    return teine_result

#---------------------------------
def getSnow_kiroro():

    #キロロリゾートのゲレンデレポートのページ
    url_kiroro = 'https://www.kiroro.co.jp/ja/dashboard/'
    #HTTPリクエスト
    html_kiroro = requests.get(url_kiroro)

    #htmlの解析
    soup_kiroro = BeautifulSoup(html_kiroro.content, 'html.parser') 
    
    #リスト化されないので、それぞれを検索して値取得
    kiroro_sekisetsu = soup_kiroro.find(text='24時間降雪量').parent.next_sibling.next_sibling
    sousekisetsu_kiroro_sancho = soup_kiroro.find(text='積雪情報').parent.next_sibling.next_sibling
    sousekisetsu_kiroro_fumoto = soup_kiroro.find(text='積雪情報').parent.next_sibling.next_sibling.next_sibling.next_sibling
    kiroro_yukishitu = soup_kiroro.find(text='雪質').parent.next_sibling.next_sibling

    title_kiroro = "【キロロリゾート】"
    sekisetsu_kiroro = "24時間積雪量:" + kiroro_sekisetsu.text
    sancho_kiroro = "山頂の総積雪量:" + sousekisetsu_kiroro_sancho.text
    fumoto_kiroro = "山麓の総積雪量:" + sousekisetsu_kiroro_fumoto.text
    yukishitsu_kiroro = "雪質:" + kiroro_yukishitu.text

    kiroro_result = title_kiroro + "\n" + sekisetsu_kiroro + "\n" + sancho_kiroro + "\n" + fumoto_kiroro + "\n" + yukishitsu_kiroro

    return kiroro_result

#---------------------------------
def getSnow_Niseko_hirafu():

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

    return teine_result

#---------------------------------
def getSnow_Yubari():

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

    return teine_result

#---------------------------------
def getSnow_Asari():

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

    return teine_result

#---------------------------------
def getSnow_Bibai():

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

    return teine_result

#---------------------------------
def getSnow_All():

    #ブラウザによる違いをなくすための合言葉
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '\
         'AppleWebKit/537.36 (KHTML, like Gecko) '\
         'Chrome/67.0.3396.99 Safari/537.36 '

    #スキー場のゲレンデレポートのページ
    url_teine = 'https://sapporo-teine.com/snow/gelande-report'
    url_rusutsu = 'https://rusutsu.com/snow-and-weather-report/'
    
    #HTTPリクエスト
    html_teine = requests.get(url_teine)
    html_rusutsu = requests.get(url_rusutsu)

    #htmlの解析
    #手稲
    soup_teine = BeautifulSoup(html_teine.content, 'html.parser') 
    
    snow_teine = soup_teine.find_all("dd",{"class": "greport__data__content"})

    title_teine = "【手稲スキー場】"
    sekisetsu_teine = "24時間積雪量:" + snow_teine[0].text

    #ルスツ
    soup_rusutsu = BeautifulSoup(html_rusutsu.content, 'html.parser') 

    snow_rusutsu = soup_rusutsu.find_all("li",{"class": "status02"})

    title_rusutsu = "【ルスツスキー場】"
    sekisetsu_rusutsu = snow_rusutsu[0].contents[3].text

    All_result = title_teine + sekisetsu_teine + "\n" + title_rusutsu + sekisetsu_rusutsu

    return All_result