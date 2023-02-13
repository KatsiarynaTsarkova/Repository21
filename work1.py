import telebot

#Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения 
# пользователей в файл.

token = ""
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Вы обратились в техподдержку")    
 

@bot.message_handler(content_types=['text'])
def read_text_commands(message):
    bot.reply_to(message, "Введите текст запроса:  ") 
    data = open('messages.txt', 'a', encoding='utf-8')
    text = f'{message.from_user.first_name}-{message.from_user.id}: {message.text}'
    data.writelines(f'{text}\n')
    data.close()
        
    
bot.infinity_polling()
