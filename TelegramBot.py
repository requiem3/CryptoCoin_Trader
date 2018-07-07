from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

#*************DELETE TOKEN BEFORE PUSHING **********************
#*************DELETE TOKEN BEFORE PUSHING **********************
#*************DELETE TOKEN BEFORE PUSHING **********************
updater = Updater(token='')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="test command 1")

def caps(bot, update, args):
     text_caps = ' '.join(args).upper()
     bot.send_message(chat_id=update.message.chat_id, text=text_caps)

start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps, pass_args=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(caps_handler)

updater.start_polling()


#def start_bot(bot, update):

#def stop_bot(bot, update):

#def balance(bot, update):

#def ban_symbol(bot, update):

#def profit_for_symbol(bot, update):

#def total_profit(bot, update):

#def unban_symbol(bot, update):

#def list_all_markets(bot, update):

#def set_time_windows(bot, update):
