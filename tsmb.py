#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:06:08 2018

@author: mparvin
"""

### Debug
debug = True

import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

### This function run command and send output to user
def runCMD(bot, update):
    usercommand = update.message.text
    cmdOut = str(subprocess.Popen(usercommand,
                                  shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT))
    update.message.reply_text(cmdOut)
    
### This function ping 8.8.8.8 and send you result    
def ping8(bot, update):
    cmdOut = str(subprocess.Popen('ping 8.8.8.8 -c2',
                                  shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT))
    update.message.reply_text(cmdOut)
    
def startCMD(bot, update):
    update.message.reply_text("Welcome to TSMB bot, this is Linux server/PC manager, Please use /help and read carefully!!")

def helpCMD(bot, update):
    update.message.reply_text("This bot has access to your server/PC, So it can do anything. Please use Telegram local password to prevent others from accessing to this bot.")    

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
 
def main():
    updater = Updater("193025875:AAHZ3hIanIau-Hg04B-mZREFBjLl6GvM9fk")
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", startCMD))
    dp.add_handler(CommandHandler("ping8", ping8))
    dp.add_handler(CommandHandler("help", helpCMD))
    dp.add_handler(MessageHandler(Filters.text, runCMD))
    
    dp.add_error_handler(error)
    
    updater.start_polling()
    
    updater.idle()
    
if __name__ == '__main__':
    main()