# Музыкальный бот для Telegram

Бот создаёт персональные плейлисты на основе ваших запросов, используя искусственный интеллект GigaChat.

## 🎯 Возможности

- Генерация плейлиста из 10 песен по вашему запросу
- Умная обработка текстовых запросов (жанр, настроение, тема)
- Форматированный вывод в виде списка треков
- Обработка ошибок при невозможности генерации

## ⚙️ Установка и настройка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/ваш-репозиторий.git
cd ваш-репозиторий
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` в корне проекта:
```ini
TELEGRAM_BOT_TOKEN=ваш_токен_бота
GIGA_AUTH_KEY=ваш_API-ключ_GigaChat
```

4. Получите токены:
- Telegram Bot Token: через [@BotFather](https://t.me/BotFather)
- GigaChat API Key: [на платформе GigaChat](https://developers.sber.ru/studio/workspaces/my-space/get/gigachat-api)
## 🚀 Запуск
```bash
python src/main.py
```

## 🎮 Пример использования
1. Старт бота:
   ```
   /start
   ```
2. Отправьте запрос:
   ```
   Рок-баллады 80-х
   ```
3. Получите результат:
   ```
   • Wind Of Change — Scorpions
   • Sweet Child O' Mine — Guns N' Roses
   • ... (10 треков)
   ```

## 📁 Структура проекта
```
.
├── src/
│   ├── bot.py       - Логика работы бота
│   └── main.py      - Точка входа и конфигурация
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚠️ Важно
- Для работы требуется Python 3.9+
- Обновите зависимости при возникновении ошибок:
  ```bash
  pip install --upgrade -r requirements.txt
  ```
- При проблемах с сертификатами SSL для GigaChat может потребоваться дополнительная настройка окружения
