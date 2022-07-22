#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 19:06
# @Author  : nice
# @File    : setup.py
# @Project : zmq-consumer


import asyncio
import configparser

from loguru import logger

from sample.zmq_consumer import write_influxdb

# 日志, 每天创建一个新的log文件, 分日志级别记录日志
logger.add("./log/ZeroMQ_WARNING_Consumer_{time:%Y-%m-%d}.log", rotation="00:00", enqueue=True, encoding="utf-8",
           level="WARNING", retention='7 days')

logger.add("./log/ZeroMQ_ERROR_Consumer_{time:%Y-%m-%d}.log", rotation="00:00", enqueue=True, encoding="utf-8",
           level="ERROR", retention='30 days')

logger.add("./log/ZeroMQ_INFO_Consumer_{time:%Y-%m-%d}.log", rotation="00:00", enqueue=True, encoding="utf-8",
           level="INFO", retention='7 days')

# get influxdb config options
config = configparser.ConfigParser()
config.read("influxdb.ini", encoding="utf-8")
url = config['influxdb']['url']
token = config['influxdb']['token']
org = config['influxdb']['org']
bucket = config['influxdb']['bucket']

# get zmq config options
host = config['zmq']['host']
port = config['zmq']['port']
topic = config['zmq']['topic'].encode('utf8')

if __name__ == '__main__':
    asyncio.run(write_influxdb(url, token, org, bucket, host, port))
