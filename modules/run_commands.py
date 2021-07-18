#!/usr/bin/env python3
# -*- coding: utf-8 -*-


### This function run command and send output to user
def runCMD(bot, update):
    if not isAdmin(bot, update):
        return
    usercommand = update.message.text
    cmdProc = subprocess.Popen(usercommand,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True)
    cmdOut, cmdErr = cmdProc.communicate()
    if cmdOut:
        bot.sendMessage(text=str(cmdOut, "utf-8"), chat_id=adminCID)
    else:
        bot.sendMessage(text=str(cmdErr, "utf-8"), chat_id=adminCID)