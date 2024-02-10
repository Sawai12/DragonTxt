#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6849871840:AAFo0BbH8f2C2Rvkb7GyXUncZ5a5UyhuNh0")
    API_ID = int(os.environ.get("API_ID", "26451206"))
    API_HASH = os.environ.get("API_HASH", "32984406271d6f3945bb536671b143a7")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6830450483")
