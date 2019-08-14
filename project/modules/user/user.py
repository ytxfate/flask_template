#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
    用户模块
"""

from flask import jsonify, Response, make_response
import json

from project.common_tools.jwt_auth import JWTAuth
from project.common_tools.common_return import common_return


class UserModul:
    """
    用户模块
    """
    def __init__(self, request):
        self.request = request

    def login(self):
        ret_obj = {}
        if self.request.method == "GET":
            req_args = self.request.args
            ret_obj = {"page": "login"}
            # return jsonify(ret_obj)     # jsonify 返回 json 格式数据
            return common_return(resp=ret_obj)  # 使用 common_return 做统一返回
            
        elif self.request.method == "POST":
            req_form = self.request.form
            req_json = self.request.json
            ret_obj = {"auth": "true"}
            jwt_str = JWTAuth().encode_jwt({'user_id': '1', 'username': 'user'})
            user_info = JWTAuth().decode_jwt(jwt_str)
            # 自己封装 response
            resp = make_response(json.dumps(ret_obj, ensure_ascii=False))
            resp.status = "201"
            resp.headers["content-type"] = "application/json"
            resp.headers["Authorization"] = jwt_str
            return resp     # make_response 自己封装返回 json 格式数据，可同时设置 headers 相关值
    
    def logout(self):
        ret_obj = {"logout": "true"}
        return Response(json.dumps(ret_obj, ensure_ascii=False), mimetype='application/json')   # Response 封装返回 json 格式数据
