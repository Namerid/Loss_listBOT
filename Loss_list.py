import telebot
from telebot import types
import config 
import requests
from bs4 import BeautifulSoup
import time


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands = ['start'])
def start(message):
    sti = open('st/sticker.tgs','rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Russian losses 🇷🇺')
    item2 = types.KeyboardButton('Ukrainian losses 🇺🇦')

    markup.add(item1,item2)

    bot.send_message(message.chat.id, 'Hello, {0.first_name}!\nWhat to do?'.format(message.from_user), reply_markup = markup)



@bot.message_handler(content_types=['text'])
def lalala(message):   
    
    if message.text == 'Russian losses 🇷🇺':
        
        url_ru = 'https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html'

        r_ru = requests.get(url_ru)
        soup_ru = BeautifulSoup(r_ru.text, 'lxml')

        all_loses_ru = soup_ru.find('div', class_ = 'post-body entry-content')
        list_ru = list(all_loses_ru.find_all('h3'))
 
        text_ru = str(list_ru[0].find('span').text) + '\n\n\n'

        for n in list_ru[1:]:
            tt = str(n.text)
            if tt == '\n':
                continue
            text_ru += '▪️' + tt + '\n\n'
        
        text_ru += 'source: ' + url_ru

        bot.send_message(message.chat.id, text_ru)


    elif message.text == 'Ukrainian losses 🇺🇦':
        
        url_ua = 'https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-ukrainian.html'

        r_ua = requests.get(url_ua)
        soup_ua = BeautifulSoup(r_ua.text, 'lxml')

        all_loses_ua = soup_ua.find('div', class_ = 'post-body entry-content')
        list_ua = list(all_loses_ua.find_all('h3'))

        text_ = ''
        for i in list_ua[0].find_all('span'): text_ += i.text
        text_ua = str(text_ + '\n\n\n')

        for n in list_ua[1:]: 
            tt = str(n.text)
            if tt == '\n':
                continue
            text_ua += '▪️' + tt + '\n\n'
        text_ua += 'source: ' + url_ua

        bot.send_message(message.chat.id, text_ua)

    else:
        bot.send_message(message.chat.id, "I don't know what to say 🤷")


bot.polling (none_stop=True)