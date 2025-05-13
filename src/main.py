import os
from dotenv import load_dotenv
from src.bot import Bot


def main():
    if not load_dotenv():
        raise RuntimeError("Не удалось загрузить .env файл")

    client_id = os.getenv('GIGA_CLIENT_ID')
    client_secret = os.getenv('GIGA_CLIENT_SECRET')

    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    bot = Bot(bot_token)


if __name__ == "__main__":
    main()