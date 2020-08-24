#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  sys_config.py
@Desc :  系统配置文件
'''

# ********** 运行配置 ********** #
# 基本运行配置
app_run_conf = {
    "HOST": "127.0.0.1",
    "PORT": 5000,
    "DEBUG": True
}
# 接口前缀及版本控制
__version = "v1.0"   # 版本, 若不需要则为空
__base_prefix_path = '/api' # api 前缀

prefix_api_path = '{prefix}{version}'.format(
    prefix=__base_prefix_path,
    version=(("/" + __version) if __version else "")
)
# 密钥
SECRET_KEY = "123"

# ********** 生产 与 测试 系统切换 ********** #
# True : 生产系统
# False: 测试系统
isFormalSystem = False

