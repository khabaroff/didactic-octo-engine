from telebot import TeleBot
import config

bot = TeleBot(config.token)

from constants import messages, menu_markup, menu_buttons, books_markup, book_paths

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, messages['start'], reply_markup=menu_markup)

@bot.message_handler(regexp=menu_buttons["books"])
def handle_books(message):
    bot.send_message(message.chat.id, messages["books"], reply_markup=books_markup)

@bot.callback_query_handler(func=lambda call: call.data in book_paths)
def handle_callback(call):
    # path = call.data
    with open(call.data, "rb") as file:
        bot.send_document(call.message.chat.id, file, caption=messages["take_it"])
        bot.delete_message(call.message.chat.id, call.message.message_id)

bot.polling(none_stop=True)