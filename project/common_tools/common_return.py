#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import jsonify

from project.common_tools import http_response_code

def common_return(code=http_response_code.SUCCESS, isSuccess=True, msg="请求成功", resp={}):
    """
    接口统一返回模板
        Args:
            code:       http状态码     int      默认 200
            isSuccess:  请求成功状态    bool    默认 True
            msg:        描述            str     默认 请求成功
            resp:       返回的数据结果集  object 默认 {}
        Returns:
            return jsonify
    """
    ret_json = {
        "code": code,
        "isSuccess": isSuccess,
        "msg": msg,
        "response": resp
    }
    return jsonify(ret_json)
