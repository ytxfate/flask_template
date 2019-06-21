#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    项目相关配置
"""


# ********** 运行配置 ********** #
# 基本运行配置
app_run_config = {
    "HOST": "127.0.0.1",
    "PORT": 5000,
    "DEBUG": True
}
# 密钥
SECRET_KEY = "123"


# ********** 数据库配置 ********** #
# redis 数据库
Redis_config = {
    "HOST": "127.0.0.1",
    "PORT": 6379,
    "AUTH": False,      # AUTH 为 True 时需要进行 用户认证
    "PASSWORD": ""
}

# mongodb 数据库
MongoDB_config = {
    "URL": "127.0.0.1:27017",   # 有此项则优先用此项进行数据库连接，否则用 HOST 和 PORT 连接
    "HOST": "127.0.0.1",
    "PORT": 27017,
    "AUTH": False,      # AUTH 为 True 时需要进行 用户认证
    "USERNAME": "",
    "PASSWORD": "",
    "DEFAULT_DB": "test"
}
