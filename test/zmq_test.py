#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/21 23:03
# @Author  : nice
# @File    : zmq_test.py
# @Project : zmq-consumer
import asyncio
import configparser

import zmq
import zmq.asyncio
from loguru import logger

config = configparser.ConfigParser()
config.read("../influxdb.ini", encoding="utf-8")
# get zmq config options
host = config['zmq']['host']
port = config['zmq']['port']
topic = config['zmq']['topic'].encode('utf8')


async def zmq_consumer(host='127.0.0.1', port='5555', topic=b''):
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.SUB)
    try:
        socket.connect(f'tcp://{host}:{port}')
        socket.setsockopt(zmq.SUBSCRIBE, topic)
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    asyncio.run(zmq_consumer(host, port, topic))
