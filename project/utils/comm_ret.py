#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  comm_ret.py  
@Desc :  response 统一返回封装
'''

# Standard library imports

# Third party imports
from flask import jsonify
# Local application imports
from project.utils.resp_code import SUCCESS


def comm_ret(code: int=SUCCESS, isSuccess: bool=True,
                    msg: str="请求成功", resp: object={}):
    """
    接口统一返回模板
        @param:
            code:       http状态码      int     默认 200
            isSuccess:  请求成功状态     bool    默认 True
            msg:        描述            str     默认 请求成功
            resp:       返回的数据结果集  object 默认 {}
        @return:
            return jsonify response
    """
    ret_json = {
        "code": code,
        "isSuccess": isSuccess,
        "msg": msg,
        "resp": resp
    }
    return jsonify(ret_json)
