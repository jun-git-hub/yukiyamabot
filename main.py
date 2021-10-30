from flask import Flask, request, abort
import os
import scrape
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReplyButton, MessageAction, QuickReply,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

#@handler.add(FollowEvent)
#def handle_follow(event):
#    line_bot_api.reply_message(
#        event.reply_token,
#        TextSendMessage(text='最初はぐー')

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
    ski_area_list = ['天気予想', '降雪一覧', '手稲', 'ルスツ', '国際','キロロ' ,'ニセコ・ヒラフ' ,'夕張' ,'朝里' ,'美唄' ]
    items = [QuickReplyButton(action=MessageAction(label=f"{ski_area}", text=f"{ski_area}")) for ski_area in ski_area_list]

    now_or_fore = ['朝の降雪情報', '天気予報']
    items_2 = [QuickReplyButton(action=MessageAction(label=f"{now_fore}", text=f"{request_message} の {now_fore}")) for now_fore in now_or_fore]

    if request_message == '天気予報':
        result = '準備中'
#        result = scrape.yosou()
    elif request_message == '降雪一覧':
        result = scrape.getSnow_All()
    elif request_message == '手稲':
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text='何を確認しますか？', quick_reply=QuickReply(items=items_2))]
        )
    elif request_message == 'ルスツ':
        result = scrape.getSnow_rusutsu()
    elif request_message == '国際':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == 'キロロ':
        
    elif request_message == 'ニセコ・ヒラフ':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '夕張':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '朝里':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '美唄':
        result = 'ごめんなさい。まだ準備中です。'
#------------------------------------------
    elif request_message == '手稲 の 朝の降雪情報':
        result = scrape.getSnow_teine()
    elif request_message == '手稲 の 天気予報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == 'ルスツ の 朝の降雪情報':
        result = scrape.getSnow_teine()
    elif request_message == 'ルスツ の 天気予報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '国際 の 朝の降雪情報':
        result = scrape.getSnow_teine()
    elif request_message == '国際 の 天気予報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == 'キロロ の 朝の降雪情報':
        result = scrape.getSnow_kiroro()
    elif request_message == 'キロロ の 天気予報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == 'ニセコ・ヒラフ の 朝の降雪情報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == 'ニセコ・ヒラフ の 天気予報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '夕張 の 朝の降雪情報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '夕張 の 天気予報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '朝里 の 朝の降雪情報':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message == '朝里 の 天気予報':
        result = 'ごめんなさい。まだ準備中です。'
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