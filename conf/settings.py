#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

PARAMS = {
    "server": "192.168.1.101",
    "port": 8000,
    "url": "/assets/report/",
    "timeout": 30,
}

LOG_PATH = os.path.join(os.path.dirname(os.getcwd()), "log", "cmdb.log")