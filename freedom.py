from telegram.ext import CommandHandler, Updater
from telegram import ReplyKeyboardMarkup
import time
from datetime import date
import random
import requests

RANDOM_MSG = [
    'Осталось немного...',
    'Осталось чуть-чуть...',
    'Не сдавайся...',
    'Я верю в тебя...',
    'Перед рассветом ночь темнее всего...',
    'Соберись...',
    'Скоро всё закончится...',
    'Уже совсем рядом...',
    'Время летит...',
    'Счастье уже близко...',
    'Ты не один...',
    'Муки скоро прекратятся...',
    'Гуа близко...',
    'Скоро отпуск...',
    'Потерпи ещё немножко...',
    'Скоро ты не увидишь эти лица...',
    'Скоро ты сам будешь решать, как поступить...'
    ]

HELLO_MSG = """
Свобода неизбежна.
Запусти меня и каждый день я буду напоминать тебе, когда ты обретешь своё счастье.
Учти, меня невозможно будет остановить, как и твою приближающуюся свободу.
Если ты готов, просто нажми на кнопку, Никита.
Бот настроен так, чтобы работать только у одного....только у тебя...
"""
FREEDOM_MSG = """
„Свобода — это роскошь, которую не каждый может себе позволить.“ —  Отто фон Бисмарк

Поздравляю.....ты справился. Дальше все только в твоих руках.
"""
FREEDOM_DATE = date(2022, 6, 30)

updater = Updater(token='5155851444:AAH8thDok0GNRnNtk8vLMKivTdjMZvNZZKQ')
URL = 'https://api.thecatapi.com/v1/images/search'

def sleep():
    sum = 0
    while sum < 86400:
        response = requests.get(URL).json()
        sum += 300
        time.sleep(300)


def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat

def hello(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/freedom']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, text=HELLO_MSG, reply_markup=button)

def say(update, context):
    chat = update.effective_chat
    while FREEDOM_DATE != date.today():
        now = date.today()
        period = FREEDOM_DATE - now
        msg = f'Дней до свободы: {str(period.days)}. {random.choice(RANDOM_MSG)}'
        context.bot.send_message(chat_id=chat.id, text=msg)
        context.bot.send_photo(chat.id, get_new_image())
        sleep()
    context.bot.send_message(chat_id=chat.id, text=FREEDOM_MSG)

updater.dispatcher.add_handler(CommandHandler('freedom', say))
updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.start_polling()
updater.idle() 