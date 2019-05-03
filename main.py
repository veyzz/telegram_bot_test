import telebot
from telebot import types, apihelper
import config


apihelper.proxy = {
  'http': '213.231.1.150:44931',
  'https': '54.37.136.149:3128'
}

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def _(message):
    if message.text in config.codewords:
        yandex = types.InlineKeyboardButton(text="yandex", url="https://yandex.ru")
        menu = types.InlineKeyboardButton(text="menu", callback_data="menu")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(yandex, menu)
        message_text = '''text1
<i>text2</i>
<b>text3</b>
<code>text4</code>'''
        bot.send_message(message.chat.id, message_text, reply_markup=keyboard, parse_mode='html')


@bot.callback_query_handler(func=lambda c: True)
def _(c):
    if c.data == "menu":
        button1 = types.InlineKeyboardButton(text="button1", callback_data="button1")
        button2 = types.InlineKeyboardButton(text="button2", callback_data="button2")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(button1, button2)
        message_text = '👍😊😄😝😞😳😐👊'
        bot.edit_message_text(message_text, c.message.chat.id, c.message.message_id, reply_markup=keyboard)


bot.polling(none_stop = True)