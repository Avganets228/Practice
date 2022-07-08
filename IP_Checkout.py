import os
import telebot
import time

hostname = ['tayle.com', 'tayle.ru']
chanel = '@test'
token = 'abcdef'


for domain in hostname:
    response = os.system('ping' + domain)
    bot = telebot.TeleBot(token)
    if response == 0:
        print(domain + ' is up.')
    else:
        print(domain + ' is down.')
        bot.send_message(chanel, domain + ' is down.')
    time.sleep(300)
