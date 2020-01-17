#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  resp_return_way.py
@Desc :  response 返回的方式
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import jsonify, Response, make_response
import json
import flask
# User-defined Modules


class RespReturnWay:
    """
    用户模块
    """
    def __init__(self, request: flask.Request):
        self.request = request

    def use_jsonify(self):
        return jsonify({'way': 'jsonify'})
    
    def use_make_response(self):
        # 自己封装 response
        resp = make_response(
            json.dumps({'way': "make_response"}, ensure_ascii=False))
        resp.status = "201"
        resp.headers["content-type"] = "application/json"
        resp.headers["Authorization"] = "jwt_str"
        return resp     # make_response 自己封装返回 json 格式数据，
                        # 可同时设置 headers 相关值
    
    def use_response(self):
        return Response(
            json.dumps({'way': "Response"}, ensure_ascii=False),
            mimetype='application/json'
        )   # Response 封装返回 json 格式数据
