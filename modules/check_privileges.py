#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser

config = configparser.ConfigParser()
config.read(".env")
blackList = config["CommandsList"]["black_list"]
whiteList = config["CommandsList"]["white_list"]


def checkPrivilege(userCommand):
    if userCommand in whiteList or userCommand not in blackList:
        return True
    return False