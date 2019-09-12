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

# User-defined Modules
from project.common_tools.jwt_auth import JWTAuth
from project.common_tools.common_return import common_return
from project.common_tools import http_response_code as H_R_C
from project.common_tools.check_and_handle_request_param import CheckAndHandleRequestParam

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
        must_need_keys = ['username', 'password']
        check_status, req_dict = CheckAndHandleRequestParam(req_dict).main_contraller(
            remove_spaces=True, must_need_keys=must_need_keys,
            can_change_keys=[], need_regexp_keys=[]
        )   # 默认值相同字段可省略
        if check_status:
            user_info = {'username': req_dict['username']}
            create_status, jwt_str, refresh_jwt_str = JWTAuth().create_jwt_and_refresh_jwt(user_info)
            if create_status:
                return common_return(resp={'jwt': jwt_str, 'refresh_jwt': refresh_jwt_str})
            else:
                return common_return(code=H_R_C.JWT_CREATE_ERROR, isSuccess=False, msg="JWT 信息生成异常")
        else:
            return common_return(code=H_R_C.PARAMETER_ERROR, isSuccess=False, msg="请求参数错误")
    
    def refresh_login_status(self):
        """
        刷新登录状态
        """
        req_dict = copy.deepcopy(self.request.json)
        must_need_keys = ['refresh_jwt']
        jwt_str = self.request.headers.get('Authorization')
        check_status, req_dict = CheckAndHandleRequestParam(req_dict).main_contraller(
            must_need_keys=must_need_keys
        )
        if check_status and jwt_str:
            decode_status, _ = JWTAuth().decode_jwt(req_dict['refresh_jwt'])
            user_info = JWTAuth().decode_jwt_without_check(jwt_str)
            if decode_status:
                create_status, jwt_str, refresh_jwt_str = JWTAuth().create_jwt_and_refresh_jwt(user_info)
                if create_status:
                    return common_return(resp={'jwt': jwt_str, 'refresh_jwt': refresh_jwt_str})
                else:
                    return common_return(code=H_R_C.JWT_CREATE_ERROR, isSuccess=False, msg="JWT 信息生成异常")
            else:
                # 跳转到登录界面 ???
                return common_return(code=H_R_C.USER_NO_LOGIN, isSuccess=False, msg="刷新 jwt 失败，重新登录")
        else:
            return common_return(code=H_R_C.PARAMETER_ERROR, isSuccess=False, msg="请求参数错误")
    
    def logout(self):
        """
        登出
        """
        # jwt 做 用户认证 时，不存在可以注销的说法
        return common_return(code=H_R_C.USER_LOGOUT, isSuccess=False, msg="用户登出", resp=g.user_info)
