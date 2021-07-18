#!/usr/bin/env python3
# -*- coding: utf-8 -*-


### This function ping 8.8.8.8 and send you result
def ping8(bot, update):
    if not isAdmin(bot, update):
        return
    cmdOut = str(
        subprocess.check_output("ping",
                                "8.8.8.8 -c4",
                                stderr=subprocess.STDOUT,
                                shell=True),
        "utf-8",
    )
    bot.sendMessage(text=cmdOut, chat_id=adminCID)
