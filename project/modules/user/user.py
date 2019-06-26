#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    用户模块
"""

from flask import jsonify, Response, make_response
import json

from project.common_tools.jwt_auth import JWTAuth

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
            return jsonify(ret_obj)
            
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
            return resp
    
    def logout(self):
        ret_obj = {"logout": "true"}
        return Response(json.dumps(ret_obj, ensure_ascii=False), mimetype='application/json')