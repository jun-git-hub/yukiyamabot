from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FollowEvent, FlexSendMessage, StickerSendMessage
)
import os
import scrape
import json

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

    if request_message == '手稲':
        result = scrape.getSnow_teine()
    elif request_message == 'ルスツ':
        result = scrape.getSnow_rusutsu()
    else:
        result = '内容を確認して、再度入力してください。'

    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=result), TextSendMessage(text='★違うスキー場も見るなら、再度選んでね。見ボタンにしたいところ★')]
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