#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 22:48
# @Author  : nice
# @File    : test.py
# @Project : zmq-consumer

import zmq
from loguru import logger

from msg2point_V1 import *

context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.connect("tcp://127.0.0.1:5555")
socket.connect('tcp://121.36.69.62:5555')
# socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.setsockopt(zmq.SUBSCRIBE, b'')

# logger.add('{time:%Y-%m-%d}_amon.log')

while True:
    response = socket.recv_string()
    response = response.splitlines()[1]
    amon_dict = amon2dict(response)

    if amon_dict.get('type') == 108:
        print(f"{amon_dict.get('type')} --- {type(amon_dict.get('type'))}")
        print(f"name: {amon_dict.get('name')}")
        print(f"timestamp: {amon_dict.get('timestamp')} {type(amon_dict.get('timestamp'))}")
        print(amon_dict)

        for value in amon_dict['data']:
            print(f"{value.get('CL_AP_ETH_STATS_SPEED')} ---- {type(value.get('CL_AP_ETH_STATS_SPEED'))}")
            print(f"{value.get('CL_AP_ETH_STATS_OPERSTATE')} ---- {type(value.get('CL_AP_ETH_STATS_OPERSTATE'))}")

        print('-+-' * 30)
    logger.info(response)
