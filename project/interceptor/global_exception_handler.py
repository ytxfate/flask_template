#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  global_exception_handler.py
@Desc :  全局异常处理
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import request
from werkzeug.exceptions import HTTPException
import logging
# User-defined Modules
from ..app import app
from ..utils.comm_ret import comm_ret
from ..utils import resp_code

logger = logging.getLogger('exception')

@app.errorhandler(Exception)
def global_exception_handler(exp):
    # 获取请求中的参数，以判断哪个链接的哪个位置有 bug
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
    try:
        req_data = "having data" if bool(request.get_data()) else "not any data"
    except Exception as e:
        req_data = {"ERROR": str(e)}
    # 记录异常信息
    logger.error("Exception => " + str(exp) +
                     "\n****** REQUEST DETAIL ******" +
                     "\n  url:  " + request.base_url +
                     "\n  args: " + str(req_args) +
                     "\n  form: " + str(req_form) +
                     "\n  json: " + str(req_json) +
                     "\n  data: " + str(req_data) +
                     "\n****************************"
                     )
    if isinstance(exp, HTTPException):
        return comm_ret(code=resp_code.EXCEPTION_ERROR,
                        isSuccess=False, msg="HTTP Exception")
    else:
        # 若果不是 HTTPException 异常，则记录具体的异常信息
        logger.exception(exp)
        return comm_ret(code=resp_code.EXCEPTION_ERROR,
                        isSuccess=False, msg="Exception")
