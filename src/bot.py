import telebot

class Bot:
    def __init__(self, bot_token):
        self.bot = telebot.TeleBot(bot_token)

        @self.bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            self.bot.reply_to(message, """\
        Hi there, I am EchoBot.
        I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
        """)

