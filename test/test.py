#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 22:48
# @Author  : nice
# @File    : test.py
# @Project : zmq-consumer

import zmq
from loguru import logger

from msg2point import *

context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.connect("tcp://127.0.0.1:5555")
socket.connect('tcp://121.36.69.62:5555')
# socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.setsockopt(zmq.SUBSCRIBE, b'')

logger.add('{time:%Y-%m-%d}_amon.log')

while True:
    response = socket.recv_string()
    # response = json.loads(response)
    response = response.splitlines()[1]
    # response = json.loads(response)
    result = amon2dict(response)
    print(result['data'][0])
    # logger.info(response)
