#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    用户模块
"""

from flask import jsonify, Response

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
            return jsonify(ret_obj)
    
    def logout(self):
        ret_obj = {"logout": "true"}
        return jsonify(ret_obj)
