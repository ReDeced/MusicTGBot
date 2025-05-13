import telebot
import json
from gigachat import GigaChat


def generate_prompt(message):
    return f'Напиши плейлист из 10 песен по следующему запросу: {message}. ' +\
    'Формат ответа: JSON {"songs": [{"author": "Автор песни", "name": "Название песни"}], ' +\
    '"response_error": {"status": "false", "message": "None"}} ' +\
    'Если ты не можешь создать плейлист по запросу, то ответ будет следующим: ' +\
    'JSON {"response_error": {"status": "true", "message": "Я не могу предоставить вам плейлист ' +\
    f'с песнями по запросу «{message}». Если у вас есть другой запрос,' +\
    'буду рад помочь!"}} ПОМНИ, ЧТО ОТВЕТ ЭТО ТОЛЬКО ТЕКСТ В ФОРМАТЕ JSON'


class Bot:
    def __init__(self, bot_token, auth_key):
        self.bot = telebot.TeleBot(bot_token)
        self.credentials = auth_key

        self.handle_start()
        self.handle_message()

        self.bot.infinity_polling()

    def handle_start(self):
        @self.bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            self.bot.reply_to(message, """\
        Привет, я буду составлять тебе список песен, по жанру выбранному тобой, и твоему настроению.\
        """)

    def handle_message(self):
        @self.bot.message_handler(func=lambda message: True)
        def echo_message(message):
            delete_message = self.bot.send_message(message.chat.id, "Обрабатываю ваш зарос")
            with GigaChat(credentials=self.credentials,verify_ssl_certs=False, model="GigaChat-Max") as gigachat:
                try:
                    response = gigachat.chat(generate_prompt(message.text))
                    response = response.choices[0].message.content
                    response = response[8:-4]
                    response = json.loads(response)
                    if response["response_error"]["status"] == "true":
                        self.bot.reply_to(message, response["response_error"]["message"])
                    else:
                        response_message = ""
                        for song in response["songs"]:
                            response_message += f'• {song["name"]} — {song["author"]}\n'
                        self.bot.reply_to(message, response_message)
                except Exception as e:
                    print(e)
                    self.bot.reply_to(message, "Ошибка, попробуйте ещё раз немного позже")

            self.bot.delete_message(delete_message.chat.id, delete_message.id)
