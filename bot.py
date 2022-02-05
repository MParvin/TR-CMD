#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:06:08 2018

@author: mparvin
"""

import subprocess
import configparser
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


config = configparser.ConfigParser()
config.read("config")
### Get admin chat_id from config file
### For more security replies only send to admin chat_id
adminCID = config["SecretConfig"]["admincid"]

### Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
### This function run command and send output to user
def runCMD(bot, update):
    if not isAdmin(bot, update):
        return
    usercommand = update.message.text
    cmdProc = subprocess.Popen(
        usercommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    cmdOut, cmdErr = cmdProc.communicate()
    if cmdOut:
        bot.sendMessage(text=str(cmdOut, "utf-8"), chat_id=adminCID)
    else:
        bot.sendMessage(text=str(cmdErr, "utf-8"), chat_id=adminCID)


### This function ping 8.8.8.8 and send you result
def ping8(bot, update):
    if not isAdmin(bot, update):
        return
    cmdOut = str(
        subprocess.check_output(
            "ping", "8.8.8.8 -c4", stderr=subprocess.STDOUT, shell=True
        ),
        "utf-8",
    )
    bot.sendMessage(text=cmdOut, chat_id=adminCID)


def startCMD(bot, update):
    if not isAdmin(bot, update):
        return
    bot.sendMessage(
        text="Welcome to TSMB bot, this is Linux server/PC manager, Please use /help and read carefully!!",
        chat_id=adminCID,
    )


def helpCMD(bot, update):
    if not isAdmin(bot, update):
        return
    bot.sendMessage(
        text="This bot has access to your server/PC, So it can do anything. Please use Telegram local password to prevent others from accessing to this bot.",
        chat_id=adminCID,
    )


def topCMD(bot, update):
    if not isAdmin(bot, update):
        return
    cmdOut = str(subprocess.check_output("top -n 1", shell=True), "utf-8")
    bot.sendMessage(text=cmdOut, chat_id=adminCID)
    bot.sendMessage(text=cmdOut, chat_id=adminCID)


def HTopCMD(bot, update):
    ## Is this user admin?
    if not isAdmin(bot, update):
        return
    ## Checking requirements on your system
    htopCheck = subprocess.call(["which", "htop"])
    if htopCheck != 0:
        bot.sendMessage(
            text="htop is not installed on your system, Please install it first and try again",
            chat_id=adminCID,
        )
        return
    ahaCheck = subprocess.call(["which", "aha"])
    if ahaCheck != 0:
        bot.sendMessage(
            text="aha is not installed on your system, Please install it first and try again",
            chat_id=adminCID,
        )
        return
    os.system("echo q | htop | aha --black --line-fix  > ./htop-output.html")
    with open("./htop-output.html", "rb") as fileToSend:
        bot.sendDocument(document=fileToSend, chat_id=adminCID)
    if os.path.exists("./htop-output.html"):
        os.remove("./htop-output.html")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def isAdmin(bot, update):
    chat_id = update.message.chat_id
    if str(chat_id) == adminCID:
        return True
    
    update.message.reply_text(
        "You cannot use this bot, because you are not Admin!!!!"
    )
    alertMessage = """Some one try to use this bot with this information:\n chat_id is {} and username is {} """.format(
        update.message.chat_id, update.message.from_user.username
    )
    bot.sendMessage(text=alertMessage, chat_id=adminCID)
    return False


def main():
    updater = Updater(config["SecretConfig"]["Token"])
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


if __name__ == "__main__":
    main()
