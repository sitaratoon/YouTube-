# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/m4mallu/inine-tube-mate
# Author   : Renjith Mangal [ https://t.me/space4renjith ]
# Credits  : https://github.com/SpEcHiDe/AnyDLBot


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7707522221:AAFEc5JiXCPydeA3bTN77a8L1M0IwtMgd-M")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "18946488"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")

    # Authorized user ids to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "-1002355394644").split())

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
