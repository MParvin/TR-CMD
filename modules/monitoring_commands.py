#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
            text=
            "htop is not installed on your system, Please install it first and try again",
            chat_id=adminCID,
        )
        return
    ahaCheck = subprocess.call(["which", "aha"])
    if ahaCheck != 0:
        bot.sendMessage(
            text=
            "aha is not installed on your system, Please install it first and try again",
            chat_id=adminCID,
        )
        return
    os.system("echo q | htop | aha --black --line-fix  > ./htop-output.html")
    with open("./htop-output.html", "rb") as fileToSend:
        bot.sendDocument(document=fileToSend, chat_id=adminCID)
    if os.path.exists("./htop-output.html"):
        os.remove("./htop-output.html")
