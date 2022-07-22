#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 21:39
# @Author  : nice
# @File    : zmq_consumer.py
# @Project : apuer

import zmq
import zmq.asyncio
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from sample.msg2point import *


# 日志, 每天创建一个新的log文件
# 注释该行，set.py 添加该代码，其他地方定义无意义
# logger.add("../log/zmq_consumer_{time:%Y-%m-%d}.log", rotation="00:00", enqueue=True, encoding="utf-8")


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
        async with InfluxDBClientAsync(url, token, org) as client:
            write_api = client.write_api()
    except Exception as e:
        logger.error(e)

    # _point1 = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
    # _point2 = Point("my_measurement").tag("location", "New York").field("temperature", 24.3)
    # response = [_point1,_point2]
    while True:
        try:
            # socket.recv_string(), 默认utf-8解码，也可以socket.recv(), 然后在通过decode('utf-8')解码
            response = await socket.recv_string()
            # 基于response的数据变换为influxdb的数据格式Point
            points = amon2point(response)
            if points:
                try:
                    async with InfluxDBClientAsync(url, token, org) as client:
                        write_api = client.write_api()
                        write_result = await write_api.write(bucket=bucket, record=points)
                        logger.info(f'amon msg {write_result} writing into influxDB ---> consumed')
                except Exception as e:
                    logger.error(e)
                    continue
        except Exception as e:
            logger.error(e)
            continue
