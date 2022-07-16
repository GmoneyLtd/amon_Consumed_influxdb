#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 21:39
# @Author  : nice
# @File    : zmq_consumer.py
# @Project : apuer

import json

import zmq
import zmq.asyncio
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from loguru import logger

# 日志, 每天创建一个新的log文件
logger.add("../log/zmqconsumer_{time}.log", rotation="00:00", enqueue=True, encoding="utf-8")


# subscribers msg ,topic = b'' or topic = ''.encode('utf-8')
async def write_influxdb(url, token, org, bucket, host='127.0.0.1', port='5555', topic=b''):
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.SUB)
    try:
        socket.connect(f'tcp://{host}:{port}')
        socket.setsockopt(zmq.SUBSCRIBE, topic)
    except Exception as e:
        logger.error(e)

    try:
        with InfluxDBClientAsync(url, token, org) as client:
            write_api = client.write_api()
    except Exception as e:
        logger.error(e)

    while True:
        try:
            response = await socket.recv()
            response = json.loads(response.decode('utf-8'))
            await write_api.write(bucket=bucket, record=response)
        except Exception as e:
            logger.error(e)
            break
