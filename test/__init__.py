#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 19:05
# @Author  : nice
# @File    : __init__.py.py
# @Project : zmq-consumer

from loguru import logger

# 日志, 每天创建一个新的log文件
logger.add("../log/testPackage_{time:%Y-%m-%d}.log", rotation="00:00", enqueue=True, encoding="utf-8")
