#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def isAdmin(bot, update):
    chat_id = update.message.chat_id
    if str(chat_id) == adminCID:
        return True
    else:
        update.message.reply_text(
            "You cannot use this bot, because you are not Admin!!!!")
        alertMessage = """Some one try to use this bot with this information:\n chat_id is {} and username is {} """.format(
            update.message.chat_id, update.message.from_user.username)
        bot.sendMessage(text=alertMessage, chat_id=adminCID)
        return False