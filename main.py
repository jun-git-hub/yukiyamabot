from flask import Flask, request, abort
import os
import scrape
import weatherfore
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReplyButton, MessageAction, QuickReply, FollowEvent
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@handler.add(FollowEvent)
def handle_follow(event):
    first_message = 'はじめまして。yukiyamabotです。\n私はおかべさんによって作られました。\nまだ準備中のところもありますが、シーズンにむけて少しずつ整備していくのでお待ち下さい。\nまた、なにか不具合や追加してほしい機能等あれば、気軽におかべさんまでご連絡ください。'
    ski_area_list = ['降雪一覧', '手稲', 'ルスツ', '国際','キロロ' ,'ニセコ・ヒラフ' ,'夕張' ,'朝里' ]
    items = [QuickReplyButton(action=MessageAction(label=f"{ski_area}", text=f"{ski_area}")) for ski_area in ski_area_list]
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=first_message), TextSendMessage(text='早速、行く予定のスキー場を選んでみよう！', quick_reply=QuickReply(items=items))]
    )

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    request_message = event.message.text
    ski_area_list = ['降雪一覧', '手稲', 'ルスツ', '国際', 'キロロ', 'ニセコ・ヒラフ', '朝里']
    items = [QuickReplyButton(action=MessageAction(label=f"{ski_area}", text=f"{ski_area}")) for ski_area in ski_area_list]

    now_or_fore = ['朝の降雪情報', '天気予報']
    items_2 = [QuickReplyButton(action=MessageAction(label=f"{now_fore}", text=f"{request_message} の {now_fore}")) for now_fore in now_or_fore]

    if request_message == '降雪一覧':
        result = scrape.getSnow_All()
    elif request_message == '手稲' or request_message == 'ルスツ' or request_message == '国際' or request_message == 'キロロ' or request_message == 'ニセコ・ヒラフ' or request_message == '夕張' or request_message ==  '朝里':
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text='何を確認しますか？', quick_reply=QuickReply(items=items_2))]
        )
#------------------------------------------
    elif request_message == '手稲 の 朝の降雪情報':
        result = scrape.getSnow_teine()
    elif request_message == 'ルスツ の 朝の降雪情報':
        result = scrape.getSnow_rusutsu()
    elif request_message == '国際 の 朝の降雪情報':
        result = 'ごめんなさい。まだ準備中です。\nhttps://www.sapporo-kokusai.jp/'
    elif request_message == 'キロロ の 朝の降雪情報':
        result = scrape.getSnow_kiroro()
    elif request_message == 'ニセコ・ヒラフ の 朝の降雪情報':
        result = 'ごめんなさい。まだ準備中です。\nhttps://www.grand-hirafu.jp/winter/gelande/business_hours/'
    elif request_message == '夕張 の 朝の降雪情報':
        result = 'ごめんなさい。まだ準備中です。\n'
    elif request_message == '朝里 の 朝の降雪情報':
        result = 'ごめんなさい。まだ準備中です。\nhttps://asari-ski.com/'
#-------------------------------------------
    elif request_message == '手稲 の 天気予報':
        result = weatherfore.getWeather(141.1998761169903, 43.07739047958601)
    elif request_message == 'ルスツ の 天気予報':
        result = weatherfore.getWeather(140.8979434319387, 42.75160066509518)
    elif request_message == '国際 の 天気予報':
        result = weatherfore.getWeather(141.08265377227207, 43.07277387513593)
    elif request_message == 'キロロ の 天気予報':
        result = weatherfore.getWeather(140.98941768826262, 43.06829870927434)
    elif request_message == 'ニセコ・ヒラフ の 天気予報':
        result = weatherfore.getWeather(140.6984933862197, 42.862056223792045)
    elif request_message == '夕張 の 天気予報':
        result = weatherfore.getWeather(141.9693637694675, 43.051062010732416)
    elif request_message == '朝里 の 天気予報':
        result = weatherfore.getWeather(141.03672335380196, 43.14336386412604)
#-----------------------------------------
    else:
        result = '内容を確認して、再度入力してね。'

    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=result), TextSendMessage(text='違うスキー場も見るなら、もう一回選んでね。', quick_reply=QuickReply(items=items))]
    )

@handler.default()
def default(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='どこの'))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)