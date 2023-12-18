import config
import telebot
from telebot import types
import requests
import json
import datetime
import defs
#from telegram.ext import Updater, CommandHandler
#import telegram.ext

bot = telebot.TeleBot(config.TOKEN, parse_mode='html')

@bot.message_handler(commands=['start'])
def start_command(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton('Показать статистику')
    markup.add(button)

    bot.send_message(message.chat.id, "Здравствуйте, я - Express Gov4c Analytics bot.", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'показать статистику':
        final_message = f"<u>Данные за всё время:</u>\n\n" \
                        + f'Общее количество заказов: ' + str(defs.number_wt()) + '\n' \
                        + f"Успешно завершенных заказов: " + str(defs.success_ended_wt()) + '\n' \
                        + f"Заказы в процессе: " + str(defs.processing_wt()) + '\n' \
                        + f"Отказано клиентом: " + str(defs.customer_refused_wt()) + '\n' \
                        + f"Отправлено курьером: " + str(defs.shipped_wt()) + '\n\n\n' \
                        + f"<u>Данные за сегодня:</u>\n\n" \
                        + f'Общее количество заказов: ' + str(defs.number_t()) + '\n' \
                        + f"Успешно завершенных заказов: " + str(defs.success_ended_t()) + '\n' \
                        + f"Заказы в процессе: " + str(defs.processing_t()) + '\n' \
                        + f"Отказано клиентом: " + str(defs.customer_refused_t()) + '\n' \
                        + f"Отправлено курьером: " + str(defs.shipped_t())

        bot.send_message(message.chat.id, final_message, parse_mode='html')

# def callback_alarm(context: telegram.ext.CallbackContext):
#     bot.send_message(message.chat.id, text=mess)
#
# def reminder(update,context):
#     bot.send_message(message.chat.id, text=mess)
#     context.job_queue.run_daily(callback_alarm, context=update.message.chat_id,days=(0, 1, 2, 3, 4, 5, 6),time = time(hour = 00, minute = 52, second = 00))

bot.polling(none_stop=True)
