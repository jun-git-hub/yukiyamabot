import os
import scrape
import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction

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

#ボタンの作成
def make_button_template():
    message_template = TemplateSendMessage(
        alt_text="どこのスキー場に行く予定？",
        template=ButtonsTemplate(
        alt_text="どこのスキー場に行く予定？",
            title="どこがいいかな",
            thumbnail_image_url="https://任意の画像URL.jpg",
            actions=[
                MessageAction(
                label='手稲',
                text='手稲'
                ),
            ]
        )
    )
    return message_template

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

    #返答に対しての関数選択
    if request_message == '手稲':
        result = scrape.getSnow_teine()
    elif request_message == 'ルスツ':
        result = scrape.getSnow_rusutsu()
    else:
        result = '内容を確認して、再度入力してね。'

    buttons = make_button_template()

    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=result), buttons]
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