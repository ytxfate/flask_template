#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  user.py
@Desc :  用户管理模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import jsonify, Response, make_response, g
import json
import copy
import flask
# User-defined Modules
from project.utils.jwt_auth import JWTAuth
from project.utils.comm_ret import comm_ret
from project.utils import resp_code
from project.utils.handle_req_param import HandleReqParam

class UserModul:
    """
    用户模块
    """
    def __init__(self, request: flask.Request):
        self.request = request

    def login(self):
        """
        登录
        """
        req_dict = copy.deepcopy(self.request.json)
        must_need_keys = ['username', 'password']
        check_status, req_dict = HandleReqParam(req_dict).main_contraller(
            rm_spaces=True, required_keys=must_need_keys,
            allow_keys=[], regexp_keys=[]
        )   # 默认值相同字段可省略
        if check_status:
            user_info = {'username': req_dict['username']}
            create_status, jwt, refresh_jwt = JWTAuth().create_jwt_and_refresh_jwt(user_info)
            if create_status:
                return comm_ret(resp={'jwt': jwt, 'refresh_jwt': refresh_jwt})
            else:
                return comm_ret(
                    code=resp_code.JWT_CREATE_ERROR, msg="JWT 信息生成异常")
        else:
            return comm_ret(code=resp_code.PARAMETER_ERROR, msg="请求参数错误")
    
    def refresh_login_status(self):
        """
        刷新登录状态
        """
        req_dict = copy.deepcopy(self.request.json)
        must_need_keys = ['refresh_jwt']
        jwt_str = self.request.headers.get('Authorization')
        check_status, req_dict = HandleReqParam(req_dict).main_contraller(
            required_keys=must_need_keys
        )
        if check_status and jwt_str:
            decode_status, _ = JWTAuth().decode_jwt(req_dict['refresh_jwt'])
            user_info = JWTAuth().decode_jwt_without_check(jwt_str)
            if decode_status:
                create_status, jwt_str, refresh_jwt_str = JWTAuth().create_jwt_and_refresh_jwt(user_info)
                if create_status:
                    return comm_ret(
                        resp={'jwt': jwt_str, 'refresh_jwt': refresh_jwt_str})
                else:
                    return comm_ret(
                        code=resp_code.JWT_CREATE_ERROR, msg="JWT 信息生成异常")
            else:
                # 跳转到登录界面 ???
                return comm_ret(
                    code=resp_code.USER_NO_LOGIN, msg="刷新 jwt 失败，重新登录")
        else:
            return comm_ret(code=resp_code.PARAMETER_ERROR, msg="请求参数错误")
    
    def logout(self):
        """
        登出
        """
        # jwt 做 用户认证 时，不存在可以注销的说法
        return comm_ret(
            code=resp_code.USER_LOGOUT, msg="用户登出", resp=g.user_info)
