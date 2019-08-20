#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File :  user.py
@Desc :  用户管理模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import jsonify, Response, make_response
import json
import copy

# User-defined Modules
from project.common_tools.jwt_auth import JWTAuth
from project.common_tools.common_return import common_return
from project.common_tools.check_request_param import check_param_must_keys
from project.common_tools import http_response_code


class UserModul:
    """
    用户模块
    """
    def __init__(self, request):
        self.request = request

    def login(self):
        """
        登录
        """
        req_dict = copy.deepcopy(self.request.json)
        must_key_collection = ['username', 'password']
        check_param_must_status = check_param_must_keys(must_key_collection, req_dict)
        if check_param_must_status:
            user_info = {'username': req_dict['username']}
            jwt_str = JWTAuth().encode_jwt(user_info)
            if jwt_str:
                return common_return(resp={'jwt': jwt_str})
            else:
                return common_return(code=http_response_code.DATA_CREATE_ERROR, isSuccess=False, msg="JWT 信息生成异常")
        else:
            return common_return(code=http_response_code.PARAMETER_ERROR, isSuccess=False, msg="请求参数错误")
    
    def logout(self):
        """
        登出
        """
        jwt_str = self.request.headers.get('Authorization')
        # 校验 jwt 是否有效
        decode_status, user_info = JWTAuth().decode_jwt(jwt_str)
        if decode_status:
            return common_return(resp=user_info)
        else:
            return common_return(code=http_response_code.DATA_CREATE_ERROR, isSuccess=False, msg="JWT 信息解析异常")
