#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  app.py
@Desc :  项目基本配置模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import Flask, request
import flask_cors
from werkzeug.exceptions import HTTPException
from logging.config import dictConfig
from flask import g

# User-defined Modules
from project.config.sys_config import SECRET_KEY

# 日志配置
dictConfig({
    'version': 1,
    'formatters': {'default': {
        # 'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
# 密钥
app.secret_key = SECRET_KEY
# 跨域解决方案
flask_cors.CORS(app, supports_credentials=True)

# 注册蓝图
import project.blueprint_mg

# 拦截器 及 全局异常处理
import project.interceptor.before_req
import project.interceptor.global_exception_handler
