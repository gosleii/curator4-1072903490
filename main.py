import telebot

bot = telebot.TeleBot("7273161499:AAEzT66DuOTczVAf4Apv5Qc5XdKS77goo20")


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hi, bro')


@bot.message_handler(commands=['new'])
def new_handler(message):
    bot.send_message(message.chat.id, 'If you are a cool person, click on *more*', parse_mode='Markdown')


@bot.message_handler(commands=['more'])
def more_handler(message):
    bot.send_message(message.chat.id,'[SUBSCRIBE!!!\nIt is the best tik tok in your life!](https://www.tiktok.com/@pisyabobramain?_t=8og6y2CrBCL&_r=1)', parse_mode='Markdown')

@bot.message_handler(commands=['check'])
def check_handler(message):
    bot.send_message(message.chat.id, '[Смотри на нас красивых](https://sun9-8.userapi.com/impg/1qV9RrRfJfQcX8sLnZM1KmlIhMoYByw4hNTFeA/d-cZqa9pAw4.jpg?size=724x724&quality=95&sign=d66067c60e7d396ada9f0618b3c972c7&type=albm)'\
                    , parse_mode='Markdown')

@bot.message_handler(commands=['bye'])
def bye_handler(message):
    bot.send_message(message.chat.id, 'Good luck, bro!')


bot.infinity_polling()