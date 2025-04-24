import logging
from telebot import types
from telegram_bot.user_data import get_user_data, update_user_data, can_deliver
import random

logger = logging.getLogger(__name__)

def register_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start_command(message):
        user_id = message.from_user.id
        user_data = get_user_data(user_id)
        bot.send_message(
            message.chat.id,
            "Добро пожаловать в симулятор доставки посылок!",
            reply_markup=create_main_menu_markup()
        )
        logger.info(f"Пользователь {user_id} начал работу с ботом")

    @bot.message_handler(commands=['raznos'])
    def raznos_command(message):
        user_id = message.from_user.id
        can_do, remaining = can_deliver(user_id)
        if not can_do:
            bot.reply_to(message, f"⏱ Подождите {remaining} секунд.")
            return
        earnings = random.randint(100, 300)
        original, buffed = update_user_data(user_id, 1, earnings)
        bot.send_message(
            message.chat.id,
            f"✅ Доставка завершена! Заработано: {buffed} руб."
        )
        logger.info(f"Пользователь {user_id} выполнил доставку, заработал {buffed} руб.")

def create_main_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("/raznos"))
    return markup
