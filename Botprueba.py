from IdBot import *
import time 
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)
usuarios = []
# comandos

@bot.message_handler(commands=["start"])

def cmd_start(message):
    bot.reply_to(message,"hola")
    
@bot.message_handler(content_types=["text"])

def bot_mensajes_texto(message):
    print(message)
    usuarios.append(message.from_user.id)
    print(message)
    if message.text.startswith("/"):
        bot.send_message(message.chat.id,"recibi comando")
    else:
        bot.send_message(message.chat.id,"recibi texto")
        for i in range(10):
            bot.send_message(message.chat.id,"esto es spam")
            time.sleep(5)
        

#def new_message_new_user(message):
    

if __name__=='__main__':
    print('iniciando bot')
    #bot.send_message(5173960385,"mensaje automatico")
    bot.infinity_polling()
    print('fin')
