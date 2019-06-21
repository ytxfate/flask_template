#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    用户模块
"""

from flask import jsonify

class UserModul:
    """
    用户模块
    """
    def __init__(self, request):
        self.request = request

    def login(self):
        ret_obj = {}
        if self.request.method == "GET":
            args = self.request.args
            print(args.get('id'))
            ret_obj = {"page": "login"}
            return jsonify(ret_obj)
            
        elif self.request.method == "POST":
            form_data = self.request.form
            print(form_data.get("username"))
            request_json = self.request.json
            print(request_json)
            ret_obj = {"auth": "true"}
            return jsonify(ret_obj)
    
    def logout(self):
        ret_obj = {"logout": "true"}
        return jsonify(ret_obj)
