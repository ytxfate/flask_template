#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    项目配置
"""

from flask import Flask, request
import flask_cors
from werkzeug.exceptions import HTTPException
from logging.config import dictConfig

from project.common_tools import http_response_code
from project.common_tools.common_return import common_return

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

import global_config

app = Flask(__name__)
# 密钥
app.secret_key = global_config.SECRET_KEY
# 跨域解决方案
flask_cors.CORS(app, supports_credentials=True)

# 注册蓝图
root_url = '/api'   # 当服务器使用 nginx 做反向代理的时候
                    # 可修改 root_url 已便 nginx 拦截请求
                    # 若不需要可以设置为空
from project.blueprint_manager.user_blueprint_manager import user
from project.blueprint_manager.file_upload_download import file
BLUEPRINT_LIST = [
    {"blueprint": user, "url_prefix": root_url + "/user"},
    {"blueprint": file, "url_prefix": root_url + "/file"}
]
for bp in BLUEPRINT_LIST:
    app.register_blueprint(bp['blueprint'], url_prefix=bp['url_prefix'])


# 拦截器(用于用户身份认证等...)
@app.before_request
def app_before_request():
    jwt_str = request.headers.get('Authorization')

# 全局异常处理
@app.errorhandler(Exception)
def global_exception_handler(exp):
    try:
        req_args = request.args.to_dict()
    except Exception as e:
        req_args = {"ERROR": str(e)}
    try:
        req_form = request.form.to_dict()
    except Exception as e:
        req_form = {"ERROR": str(e)}
    try:
        req_json = request.json
    except Exception as e:
        req_json = {"ERROR": str(e)}
    app.logger.error("Exception => " + str(exp) +
                     "\n****** REQUEST DETAIL ******" +
                     "\nurl:  " + request.url +
                     "\nargs: " + str(req_args) +
                     "\nform: " + str(req_form) +
                     "\njson: " + str(req_json) +
                     "\n****************************"
                     )
    if isinstance(exp, HTTPException):
        return common_return(code=http_response_code.EXCEPTION_ERROR, isSuccess=False, msg="HTTP Exception")
    else:
        return common_return(code=http_response_code.EXCEPTION_ERROR, isSuccess=False, msg="Exception")
