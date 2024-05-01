#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6996738227:AAEFQi8ej2_vz_G5UAJpwtdA251CyHbdPlQ")
    API_ID = int(os.environ.get("API_ID", "28127959"))
    API_HASH = os.environ.get("API_HASH", "0debc9c74510961fc8cf134a3c6eae0f")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6370953390")
