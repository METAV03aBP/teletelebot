import telebot
from telebot import types
import requests
from datetime import datetime


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"], ["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


f = open('/home/petro/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

f = open('/home/petro/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

token = '5129080638:AAHS7gavDnIvrY1G2ix8u0BqIlJV7BcesRk'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Crypto Price")
        markup.add(item1)
        bot.send_message(m.chat.id,
                         'This is Crypto Price Bot',  reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.chat.type == 'private':
        if message.text == 'Crypto Price':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("btc_usd")
            item2 = types.KeyboardButton('ltc_usd')
            item3 = types.KeyboardButton('shib_usd')
            item4 = types.KeyboardButton('eth_usd')
            item5 = types.KeyboardButton('doge_usd')
            item6 = types.KeyboardButton('dash_usd')
            item7 = types.KeyboardButton("trx_usd")
            item8 = types.KeyboardButton("zec_usd")
            item9 = types.KeyboardButton("xrp_usd")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            markup.add(item5)
            markup.add(item6)
            markup.add(item7)
            markup.add(item8)
            markup.add(item9)
            bot.send_message(message.chat.id,
                             'Pick your crypto!', reply_markup=markup)

        elif message.text == 'btc_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'ltc_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/ltc_usd")
                response = req.json()
                sell_price = response["ltc_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell LTC price: {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'eth_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                response = req.json()
                sell_price = response["eth_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price: {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'shib_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/shib_usd")
                response = req.json()
                sell_price = response["shib_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell SHIB price:"
                                 f" {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'doge_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
                response = req.json()
                sell_price = response["doge_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price: {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'dash_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/dash_usd")
                response = req.json()
                sell_price = response["dash_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DASH price: {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'trx_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/trx_usd")
                response = req.json()
                sell_price = response["trx_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell TRX price: {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'zec_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/zec_usd")
                response = req.json()
                sell_price = response["zec_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ZEC price: {sell_price}")

            except Exception as ex:
                print(ex)

        elif message.text == 'xrp_usd':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/xrp_usd")
                response = req.json()
                sell_price = response["xrp_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell XRP price: {sell_price}")

            except Exception as ex:
                print(ex)


bot.polling(none_stop=True, interval=0)
