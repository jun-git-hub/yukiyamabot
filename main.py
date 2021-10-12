from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, FlexSendMessage
)
import os

import scrape

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

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

#友達登録してくれたときに表示される
@handler.add(FollowEvent)
def handle_follow(event):
    with open('./first_message.json') as f:
        first_message = json.load(f)
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='こんにちは', contents="こんにちは。本アカウントは本日の雪山の状況を自動検索してくれるアカウントです。不具合や機能追加の希望がある方は岡部までお知らせください。" + first_message)
    )

#スクレイピングの条件分岐、実行、返信
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    request_message = event.message.text
    if request_message == "札幌国際":
        result = scrapeKokusai.getSnow()
    elif request_message == "手稲":
        result = scrapeTeine.getSnow()
    elif request_message == "ルスツ":
        result = scrapeRusutsu.getSnow()
    elif request_message == "キロロ":
        result = scrapeKiroro.getSnow()
    elif
        result = "選び直してください。"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))

#実行後のデフォルトメッセージ
@handler.default()
def default(event):
    with open('./first_message.json') as f:
        saisyohaguu_message = json.load(f)
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='どこのスキー場？', contents=first_message)
    )

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)