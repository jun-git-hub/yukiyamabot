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
    request_message_1 = event.message.text
    ski_area_list = ['降雪予想', '降雪一覧', '手稲', 'ルスツ', '国際','キロロ' ,'ニセコ・グラン・ヒラフ' ,'夕張' ,'朝里' ,'美唄' ]
    items = [QuickReplyButton(action=MessageAction(label=f"{ski_area}", text=f"{ski_area}")) for ski_area in ski_area_list]

    now_or_fore = ['降雪情報', '天気予報']

    if request_message_1 == '天気予報一覧':
        result = scrape.yosou()
    elif request_message_1 == '降雪情報一覧':
        result = scrape.getSnow_All()
    elif request_message_1 == '手稲':
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text='何を確認しますか？', quick_reply=QuickReply(items=now_or_fore))]
        )
        request_message_2 = event.message.text
        if request_message_2 == '降雪情報':
            result = scrape.getSnow_teine()
        if request_message_2 == '天気予報':
            result = 'まだです'
        else:
            result = '初めからやりなおしてね'
    elif request_message_1 == 'ルスツ':
        result = scrape.getSnow_rusutsu()
    elif request_message_1 == '国際':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message_1 == 'キロロ':
        result = scrape.getSnow_kiroro()
    elif request_message_1 == 'ニセコ・グラン・ヒラフ':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message_1 == '夕張':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message_1 == '朝里':
        result = 'ごめんなさい。まだ準備中です。'
    elif request_message_1 == '美唄':
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