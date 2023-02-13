import telebot


#Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него
# и отправлять ответ обратно пользователю.


bot = telebot.TeleBot(" ", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Добрый день, чем могу помочь?")    
    
@bot.message_handler(content_types=['text'])
def read_text_command(message):
        data =  open('messages.txt', 'r', encoding='utf-8')
        r_list = data.readlines()
        data.close()
        for id in r_list:
            bot.send_message(id[:-1], 'Переустановите систему!')#убираем последний символ \n
           
     
      
 
bot.infinity_polling()
