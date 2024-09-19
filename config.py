import os

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN', 'YOUR_BOT_TOKEN')  # Токен можно вынести в переменные окружения для безопасности.
LOG_FILE = 'bot.log'  # Лог-файл для записи событий.
