import telebot

bot = telebot.TeleBot("7273161499:AAEZK09dlMqmHwEeMnSAHzQ9cpEDU51DLQM")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привки броук')
@bot.message_handler(commands=['new'])
def new_handler(message):
    bot.send_message(message.chat.id, 'Если ты прик челик, то жмакай *more*', parse_mode='Markdown')
@bot.message_handler(command=['more'])
def more_handler(message):
    bot.send_message(message.chat.id, "[_go subscribe_](https://www.tiktok.com/@pisyabobramain?_t=8og6y2CrBCL&_r=1)", parse_mode="Markdown")
@bot.message_handler(command=["bye"])
def bye_handler(message):
    bot.send_message(message.chat.id, "*Пок*", parse_mode="Markdown")

bot.infinity_polling()