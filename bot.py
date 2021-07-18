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

config = configparser.ConfigParser()
config.read("config")
### Get admin chat_id from config file
### For more security replies only send to admin chat_id
adminCID = config["SecretConfig"]["admincid"]

# Import modules
import modules.logger
from modules.check_admin import isAdmin
from modules.run_commands import runCMD
from modules.run_ping import ping8
from modules.monitoring_commands import *


def startCMD(bot, update):
    if not isAdmin(bot, update):
        return
    bot.sendMessage(
        text=
        "Welcome to TSMB bot, this is Linux server/PC manager, Please use /help and read carefully!!",
        chat_id=adminCID,
    )


def helpCMD(bot, update):
    if not isAdmin(bot, update):
        return
    bot.sendMessage(
        text=
        "This bot has access to your server/PC, So it can do anything. Please use Telegram local password to prevent others from accessing to this bot.",
        chat_id=adminCID,
    )


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


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
