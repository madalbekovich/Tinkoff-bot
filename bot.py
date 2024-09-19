import telebot
from config import API_TOKEN
from handlers import handle_start, handle_message
from logger import logger

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    handle_start(message, bot)

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    try:
        handle_message(message, bot)
    except Exception as e:
        logger.error(f"Error while handling message from user {message.from_user.id}: {str(e)}")
        bot.reply_to(message, "Произошла ошибка. Попробуйте позже.")

if __name__ == '__main__':
    logger.info('Bot started.')
    bot.polling(none_stop=True)
