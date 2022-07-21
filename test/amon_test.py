#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 16:48
# @Author  : nice
# @File    : amon_test.py
# @Project : zmq-consumer

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "XB1gLmlbnwVLVXF6WNpPkaM4MTgBrn8yGsrdM6Pvyz3-UOUQelKZrXO4joxYd8EWwDHCMWXKEfb4OGLHrB1jcA=="
org = "arun"
bucket = "amon_test"
t1 = 1658293200

with InfluxDBClient(url="http://121.36.69.62:8086", token=token, org=org) as client:
    point = Point("ap-test").tag("ip", '192.168.1.60').field("uplink", 200).field('downlink', 200).time(
        datetime.fromtimestamp(t1), WritePrecision.S)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket, org, point)
