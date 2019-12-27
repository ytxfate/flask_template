#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  db_config.py
@Desc :  数据库配置文件
'''

# ********** 数据库配置 ********** #
# redis 数据库
REDIS_CONF = {                  # 生产系统使用
    "HOST": "127.0.0.1",
    "PORT": 6379,
    "AUTH": False,              # AUTH 为 True 时需要进行 用户认证
    "PASSWORD": "",
    "DECODE_RESPONSES": True    # 是否对查询结果进行编码处理
}
REDIS_CONF_T = {                # 测试系统使用
    "HOST": "127.0.0.1",
    "PORT": 6379,
    "AUTH": False,              # AUTH 为 True 时需要进行 用户认证
    "PASSWORD": "",
    "DECODE_RESPONSES": True    # 是否对查询结果进行编码处理
}

# mongodb 数据库
MONGODB_CONF = {                # 生产系统使用
    "URL": "127.0.0.1:27017",   # 有此项则优先用此项进行数据库连接
                                # 否则用 HOST 和 PORT 连接
    "HOST": "127.0.0.1",
    "PORT": 27017,
    "AUTH": False,              # AUTH 为 True 时需要进行 用户认证
    "USERNAME": "",
    "PASSWORD": "",
    "DEFAULT_DB": "test"        # 默认数据库
}
MONGODB_CONF_T = {              # 测试系统使用
    "URL": "127.0.0.1:27017",   # 有此项则优先用此项进行数据库连接，
                                # 否则用 HOST 和 PORT 连接
    "HOST": "127.0.0.1",
    "PORT": 27017,
    "AUTH": False,              # AUTH 为 True 时需要进行 用户认证
    "USERNAME": "",
    "PASSWORD": "",
    "DEFAULT_DB": "test"        # 默认数据库
}
