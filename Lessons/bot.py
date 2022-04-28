#5294691044:AAFdn7xtxqGRqvQqFTey6-5uZI5hNVJINYE

import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bt = telebot.TeleBot('5294691044:AAFdn7xtxqGRqvQqFTey6-5uZI5hNVJINYE')

@bt.message_handler(commands=['start'])
def start_message(message):
    bt.send_message(message.chat.id, "Hello there!")

@bt.message_handler(commands=['update'])
def update_message(message):
    
    html = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(html)

    tag_list = soup.findAll('p', {'class': 'value fall'})
    
    buy = tag_list[0].text
    sell = tag_list[1].text
    nb = tag_list[2].text

    bt.send_message(message.chat.id, buy + ', ' + sell + ', ' + nb)

bt.polling()