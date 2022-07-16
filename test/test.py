#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 22:48
# @Author  : nice
# @File    : test.py
# @Project : zmq-consumer

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.connect("tcp://127.0.0.1:5555")
socket.connect('tcp://121.36.69.62:5555')
# socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.setsockopt(zmq.SUBSCRIBE, b'')

while True:
    response = socket.recv()
    # print(type(response))
    print('-#-' * 20)
    print(response)
    print('-#-' * 20)
