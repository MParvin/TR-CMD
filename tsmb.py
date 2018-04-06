#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:06:08 2018

@author: mparvin
"""

### Debug
debug = True

import subprocess
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

### This function run command and send output to user
def runCMD(bot, update):
    usercommand = update.message.text
    cmdProc = subprocess.Popen(usercommand,
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.PIPE,
                                         shell=True)
    cmdOut, cmdErr = cmdProc.communicate()
    if cmdOut:
        update.message.reply_text(str(cmdOut,'utf-8'))
    else:
        update.message.reply_text(str(cmdErr,'utf-8'))
    
### This function ping 8.8.8.8 and send you result    
def ping8(bot, update):
    cmdOut = str(subprocess.check_output('ping' , '8.8.8.8 -c4',
                                         stderr=subprocess.STDOUT,
                                         shell=True),'utf-8')
    update.message.reply_text(cmdOut)
    
def startCMD(bot, update):
    update.message.reply_text("Welcome to TSMB bot, this is Linux server/PC manager, Please use /help and read carefully!!")

def helpCMD(bot, update):
    update.message.reply_text("This bot has access to your server/PC, So it can do anything. Please use Telegram local password to prevent others from accessing to this bot.")    

def topCMD(bot, update):
    cmdOut = str(subprocess.check_output('top -n 1',
                                  shell=True),'utf-8')
    update.message.reply_text(cmdOut)

def HTopCMD(bot, update):
    htopCheck = subprocess.call(['which','htop'])
    if htopCheck != 0:
        update.message.reply_text("htop is not installed on your system, Please install it first and try again")
        return
    ahaCheck = subprocess.call(['which','aha'])
    if ahaCheck != 0:
        update.message.reply_text("aha is not installed on your system, Please install it first and try again")
        return
    chat_id = update.message.chat_id
    os.system('echo q | htop | aha --black --line-fix  > ./htop-output.html')
    with open('./htop-output.html',"rb") as fileToSend:
        bot.sendDocument(document=fileToSend,chat_id=chat_id)
    if os.path.exists('./htop-output.html'):
        os.remove('./htop-output.html')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
 
def main():
    updater = Updater("193025875:AAHZ3hIanIau-Hg04B-mZREFBjLl6GvM9fk")
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", startCMD))
    dp.add_handler(CommandHandler("ping8", ping8))
    dp.add_handler(CommandHandler("top", topCMD))
    dp.add_handler(CommandHandler("htop", HTopCMD))
    dp.add_handler(CommandHandler("help", helpCMD))
    dp.add_handler(MessageHandler(Filters.text, runCMD))
    
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()