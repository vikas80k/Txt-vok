#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6618274486:AAESKaMTJJ0tOR62pqOPt-a0WcfpTi0y7nk")
    API_ID = int(os.environ.get("API_ID", "22694914"))
    API_HASH = os.environ.get("API_HASH", "4fd02c02368941a03d48ecab3a3b4a31")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7491374623")
