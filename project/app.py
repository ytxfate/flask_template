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

'''
# nginx 代理后获取真实ip地址
from werkzeug.serving import WSGIRequestHandler
def address_string(self):
    # 这就是在nginx的config中，为什么一定要有X-Real-IP啦
    return "[%s]-[%s]" % (self.headers.get('X-Forwarded-For', self.client_address[0]), self.headers.get('X-Real-Ip', self.client_address[0]))

WSGIRequestHandler.address_string = address_string
'''

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

# json 序列化处理
from flask.json import JSONEncoder as f_JSONEncoder
from datetime import date, datetime
class JSONEncoder(f_JSONEncoder):
    def default(self, o):   # pylint: disable=E0202
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        return super(JSONEncoder, self).default(o)


app = Flask(__name__)
# json 序列化处理
app.json_encoder = JSONEncoder
# 密钥
app.secret_key = SECRET_KEY
# 跨域解决方案
flask_cors.CORS(app, supports_credentials=True)

# 注册蓝图
import project.blueprint_mg.blueprint_mg

# 拦截器 及 全局异常处理
import project.interceptor.before_req
import project.interceptor.global_exception_handler
