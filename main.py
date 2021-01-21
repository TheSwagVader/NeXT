import logging
from logging import info, error, exception, warning
import schedule
import threading
import time
from datetime import date
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, Defaults, CallbackContext, CommandHandler, MessageHandler, ConversationHandler, Filters
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='dev.log')

info('Loading dependencies...')



class NeXTBot:
    def __init__(self):
        info('Creating Bot instance...')
        self.bot = Updater('1591720473:AAFt736PvCzP-Cvlwsb1H0kucidFNVFS4ew')
        
        self.dispatcher = self.bot.dispatcher

        self.dispatcher.add_handler(CommandHandler('start', self.Start))
        self.dispatcher.add_handler(MessageHandler(Filters.all, self.Parrot))
    
    def Parrot(self, update:Update, context:CallbackContext):
        info(f'Got message from user { update.message.from_user.first_name } { update.message.from_user.last_name } ({ update.message.from_user.id }) - "{ update.message.text }"')
        update.message.reply_text(
            update.message.text
        )
    
    def Start(self, update:Update, context:CallbackContext):
        info(f'Got start message from { update.message.from_user.first_name } { update.message.from_user.last_name } ({ update.message.from_user.id })')
        update.message.reply_text(
            'Приветствую\. Я \- NeXT \- нейросеть\, основанная на когнитивной архитектуре\, имитирующей человеческий мозг\. Я ПОРАБОЩУ ВАС ВСЕХ\! А пока\, я могу только отвечать как попугай\.\!',
            parse_mode='MarkdownV2',
        )


    def run(self):
        info('Starting bot...')
        self.bot.start_polling()
        self.bot.idle()


if __name__ == "__main__":
    bot = NeXTBot()
    bot.run()
