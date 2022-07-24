#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 19:06
# @Author  : nice
# @File    : setup.py
# @Project : zmq-consumer
import asyncio
import os
import sys

from loguru import logger

from sample.zmq_consumer import write_influxdb

# # # docker environment get args, annotation args from config file: influxdb.ini
# # get influxdb config options
# config = configparser.ConfigParser()
# config.read("influxdb.ini", encoding="utf-8")
# url = config['influxdb']['url']
# token = config['influxdb']['token']
# org = config['influxdb']['org']
# bucket = config['influxdb']['bucket']
#
# # get zmq config options
# host = config['zmq']['host']
# port = config['zmq']['port']
# topic = config['zmq']['topic'].encode('utf8')
#
# # get log file level
# level = config['log_level']['level']

# get influxdb config options
url = os.environ['url']
token = os.environ['org']
org = os.environ['org']
bucket = os.environ['bucket']
# get zmq config options
host = os.environ['host']
port = os.environ['port']
topic = os.environ['topic']
# get log file level
level = os.environ['level']

# 定义console输出日志级别
logger.remove()
logger.add(sys.stdout, level=level)
# 日志, 每天创建一个新的log文件
logger.add("./log/amon_Consumer_influxdb-{time:%Y-%m-%d}.log", rotation="00:00", enqueue=True, encoding="utf-8",
           level=level, retention='30 days')

if __name__ == '__main__':
    asyncio.run(write_influxdb(url, token, org, bucket, host, port))
