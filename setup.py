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

# 日志, 每天创建一个新的log文件
logger.add("../log/Zeromq_consumer_{time:%Y-%m-%d}.log", rotation="00:00", enqueue=True, encoding="utf-8")

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
