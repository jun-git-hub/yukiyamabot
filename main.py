#必用なものをインポート
from flask import Flask, request, abort
import os
import scrape as sc

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
#LINEでのイベントを取得
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

#アプリケーション本体をopenすると実行される
@app.route("/")
def hello_world():
    return "hello world!"

#/callback　のリンクにアクセスしたときの処理。webhook用。
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

#メッセージ受信時のイベント
#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
 #   '''
    #line_bot_apiのreply_messageメソッドでevent.message.text(ユーザのメッセージ)を返信
  #  line_bot_api.reply_message(
 #       event.reply_token,
#        TextSendMessage(text=event.message.text))
 #   '''
  #  line_bot_api.reply_message(
  #      event.reply_token,
  #      TextSendMessage(text=sc.getSnow())
  #  )

## 2 ##
###############################################
#LINEのメッセージの取得と返信内容の設定(オウム返し)
###############################################
 
#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に、
#def以下の関数を実行します。
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークンです。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡しています。
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#    line_bot_api.reply_message(
#        event.reply_token,
#        TextSendMessage(text=sc.getSnow())) #ここでオウム返しのメッセー

    word = event.message.text
    result = sc.getNews()

    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=result)
    )

if __name__ == "__main__" :
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)