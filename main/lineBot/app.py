  
from flask import Flask, request, abort
from linebot import (
     LineBotApi, WebhookHandler
 )
from linebot.exceptions import (
     InvalidSignatureError
 )
from linebot.models import *
import os
import requests

app = Flask(__name__)
# #  Channel Access Token
line_bot_api = LineBotApi('Channel Access Token')
# #  Channel Secret
handler = WebhookHandler('Channel Secret')

#  監聽所有來自 /callback 的 Post Request
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

#  處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #send online photo
    if event.message.text == "image":
        message = ImageSendMessage(original_content_url='https://ithelp.ithome.com.tw/storage/image/ironman13thsidebar.png',  preview_image_url='https://ithelp.ithome.com.tw/storage/image/ironman13thsidebar.png')
    else:  
        # return message
        message = TextSendMessage(text=event.message.text)

    line_bot_api.reply_message(event.reply_token, message)
# User ID,send message to user.
user_id = 'User ID'
@app.route("/push_function/<string:push_text_str>")
def push_message(push_text_str):
    line_bot_api.push_message(user_id, TextSendMessage(text=push_text_str))

class LintBotFunction:
     def __init__(self,push_str):
        self.push_str = push_str
        self.webhook_url = "https://linebotforcat.herokuapp.com/push_function/" 
          
     def push_message(self):
        requests.get(self.webhook_url + self.push_str)


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    push_str = "test message"
    lineBot = LintBotFunction(push_str)
    lineBot.push_message()
