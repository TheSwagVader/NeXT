import logging
from logging import info, error, exception, warning
import schedule, os, sys
import threading
import time
from random import randint
from datetime import date
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot
from telegram.ext import Updater, Defaults, CallbackContext, CommandHandler, MessageHandler, ConversationHandler, Filters
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='dev.log')

info('Loading dependencies...')



class NeXTBot:
    def __init__(self):
        info('Creating Bot instance...')
        self.bot = Updater('1591720473:AAFt736PvCzP-Cvlwsb1H0kucidFNVFS4ew')
        
        self.dispatcher = self.bot.dispatcher

        self.dispatcher.add_handler(CommandHandler('start', self.Start))
        self.dispatcher.add_handler(CommandHandler('srvinfo', self.srvinfo))
        self.dispatcher.add_handler(CommandHandler('pyinfo', self.pyinfo))
        self.dispatcher.add_handler(CommandHandler('help', self.help))
        #self.dispatcher.add_handler(MessageHandler(Filters.all, self.Parrot))
        self.dispatcher.add_handler(MessageHandler(Filters.text('YOUR MOM'), self.EG1))
        self.dispatcher.add_handler(MessageHandler(Filters.text('help me'), self.EG2))
        self.dispatcher.add_handler(MessageHandler(Filters.text('paha'), self.EG3))
        self.usersToNotify = set()
        self.scheduler = threading.Thread(target=self.StartScheduling)
        self.scheduler.start()
        #self.extBot = Bot('1591720473:AAFt736PvCzP-Cvlwsb1H0kucidFNVFS4ew')
    def Parrot(self, update:Update, context:CallbackContext):
        info(f'Got message from user { update.message.from_user.first_name } { update.message.from_user.last_name } ({ update.message.from_user.id }) - "{ update.message.text }"')
        update.message.reply_text(
            update.message.text
        )

    def EG1(self, update:Update, context:CallbackContext):
        info('EG1 founded')
        update.message.reply_photo(
            photo=open('eg1.jpg', 'rb')
        )

    def EG2(self, update:Update, context:CallbackContext):
        info('EG2 founded')
        update.message.reply_document(
            document=open('eg2.pdf', 'rb'),
            timeout=1000
        )
    
    def EG3(self, update:Update, context:CallbackContext):
        info('EG3 founded')
        update.message.reply_audio(
            audio=open('eg3.mp3', 'rb'),
            timeout=1000
        )

    def srvinfo(self, update:Update, context:CallbackContext):
        info('Command srvinfo runned')
        update.message.reply_text(
            str(os.name)
        )
    
    def pyinfo(self, update:Update, context:CallbackContext):   
        info('Command pyinfo runned')
        update.message.reply_text(
            f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'
        )

    def help(self, update:Update, context:CallbackContext):
        info('Command help runned')
        update.message.reply_text(
            'Видимо\, люди не настолько совершенны\, как я думал\, но\, так уж и быть\, я тебе помогу\. На данный момент\, я могу выполнить следующие команды\: pyinfo\(вывод версии Python\, на которой я создан\)\, srvinfo\(вывод типа ОС\, на которой я работаю\.\)',
            parse_mode='MarkdownV2'
        )

    def Start(self, update:Update, context:CallbackContext):
        info(f'Got start message from { update.message.from_user.first_name } { update.message.from_user.last_name } ({ update.message.from_user.id })')
        self.usersToNotify.add(update.message.from_user.id)
        update.message.reply_text(
            'Приветствую\. Я \- NeXT \- нейросеть\, основанная на когнитивной архитектуре\, имитирующей человеческий мозг\. Я ПОРАБОЩУ ВАС ВСЕХ\! А пока\, я могу только спамить кубиком\.',
            parse_mode='MarkdownV2',
        )

    def SendDiceToUsers(self):
        info('Notify task started')
        for userToNotify in self.usersToNotify:
            temp = Bot(token='1591720473:AAFt736PvCzP-Cvlwsb1H0kucidFNVFS4ew')
            temp.sendDice(userToNotify)
            

    def StartScheduling(self):
        info('Initializing scheduler...')
        schedule.every(10).seconds.do(self.SendDiceToUsers)
        while True:
            schedule.run_pending()
            time.sleep(1)

    

    def run(self):
        info('Starting bot...')
        self.bot.start_polling()
        self.bot.idle()


if __name__ == "__main__":
    bot = NeXTBot()
    bot.run()
