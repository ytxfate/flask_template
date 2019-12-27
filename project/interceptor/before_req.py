#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  before_req.py
@Desc :  请求拦截器
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import request, g
# User-defined Modules
from ..app import app
from ..utils.comm_ret import comm_ret
from ..utils import resp_code
from ..utils.jwt_auth import JWTAuth


@app.before_request
def app_before_request():
    # 按要求拦截请求
    req_path = request.path
    if 'user/refresh_login_status' in req_path:
        jwt_str = request.headers.get('Authorization')
        if not jwt_str:
            return comm_ret(code=resp_code.USER_NO_LOGIN, msg="请登录")
    elif any([
        ('/user/' in req_path and 'login' not in req_path)
    ]):
        # 拦截器进行用户认证，认证完成后将相关数据放到 flask 当前应用环境的通用变量 g 中，
        # 后续模块可以通过 g 对象来获取设置在其中的数据，
        # 当数据不存在时出现 '_AppCtxGlobals' object has no attribute 'xxx' 异常
        jwt_str = request.headers.get('Authorization')
        decode_status, user_info = JWTAuth().decode_jwt(jwt_str)
        g.user_info = None
        if decode_status:
            g.user_info = user_info
            # print(g.user_info)
        else:
            # 跳转到登录页面
            return comm_ret(code=resp_code.USER_NO_LOGIN, msg="请登录")
