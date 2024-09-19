from telebot import types
from logger import log_message


def handle_start(message, bot):
    bot.reply_to(message, "Добрый день! Я представляю Тинькофф Банк. У нас есть предложение кредитной карты. "
                          "Готовы выслушать детали?")
    log_message(message.from_user.id, 'Started conversation')

def handle_message(message, bot):
    log_message(message.from_user.id, message.text)
    
    if "процентная ставка" in message.text.lower():
        bot.reply_to(message, "Процентная ставка начинается от 12%. Лимит до 700 000 рублей.")
    elif "откуда у вас мой номер" in message.text.lower():
        bot.reply_to(message, "Ваш номер был в базе клиентов, которые интересовались банковскими продуктами.")
    elif "перезвоните" in message.text.lower():
        bot.reply_to(message, "Конечно, когда вам будет удобно?")
    elif "онлайн" in message.text.lower():
        bot.reply_to(message, "Да, вы можете оформить карту онлайн. Оставьте заявку на сайте.")
    else:
        bot.reply_to(message, "Могу помочь с чем-то еще?")
