import os
import telebot
from telegram_bot.handlers import register_handlers

def start_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN не установлен")
    bot = telebot.TeleBot(token)
    register_handlers(bot)
    bot.polling(none_stop=True)
