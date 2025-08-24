import os
import openai
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# Получаем ключи из переменных окружения Replit
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Проверка на наличие ключей
if not all([LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET, OPENAI_API_KEY]):
    print("Ошибка: Отсутствуют переменные окружения. Пожалуйста, убедитесь, что вы настроили все ключи на Render.com.")
    exit()

# Инициализация API
app = Flask(__name__)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
openai.api_key = OPENAI_API_KEY

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    original_text = event.message.text

    try:
        # Используем OpenAI для перевода
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI that translates messages."},
                {"role": "user", "content": f"Please translate the following text into English: {original_text}"}
            ]
        )
        translated_text = response.choices[0].message.content.strip()

        # Отправляем переведенный текст обратно пользователю
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=translated_text)
        )

    except Exception as e:
        # В случае ошибки (например, с OpenAI API)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"An error occurred: {e}")
        )
        app.logger.error(f"Error during translation: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)