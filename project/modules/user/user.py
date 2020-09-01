#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  user.py  
@Desc :  用户管理模块
'''

# Standard library imports
import copy
import json
# Third party imports
from flask import jsonify, Response, make_response, g, request, Blueprint
import flask
# Local application imports
from project.models.user.user_models import LoginInfoModel, RefreshJWTModel
from project.utils import resp_code
from project.utils.comm_ret import comm_ret
from project.utils.handle_req_param import HandleReqParam
from project.utils.jwt_auth import JWTAuth


user_router = Blueprint("user", __name__)


@user_router.route('/login', methods=["POST"])
def login():
    """
    登录
    """
    req_dict = copy.deepcopy(request.json)
    # 采用 pydantic 进行参数验证
    login_info = LoginInfoModel(**req_dict)
    user_info = {'username': login_info.username}
    status, jwt, refresh_jwt = JWTAuth().create_jwt_and_refresh_jwt(user_info)
    if status is False:
        return comm_ret(
            code=resp_code.JWT_CREATE_ERROR, msg="JWT 信息生成异常")
    return comm_ret(resp={'jwt': jwt, 'refresh_jwt': refresh_jwt})


@user_router.route('/refresh_login_status', methods=["GET"])
def refresh_login_status():
    """
    刷新登录状态
    """
    refresh_jwt = request.args.get('refresh_jwt')
    if not refresh_jwt:
        return comm_ret(code=resp_code.PARAMETER_ERROR, msg="参数异常")
    jwt_str = request.headers.get('Authorization')
    # 采用 pydantic 进行参数验证
    _ = RefreshJWTModel(**{'jwt': jwt_str, 'refresh_jwt': refresh_jwt})
    decode_status, data = JWTAuth().decode_jwt_check_refresh_jwt(jwt_str,
                                                                 refresh_jwt)
    if decode_status is False:
        return comm_ret(
                code=resp_code.USER_NO_LOGIN, msg="刷新 jwt 失败，重新登录")
    if not data:
        return comm_ret(code=resp_code.USER_NO_LOGIN,
                        msg="刷新 jwt 失败，重新登录")
    status, jwt_str, refresh_jwt_str = JWTAuth().create_jwt_and_refresh_jwt(
        data)
    if status is False:
        return comm_ret(
            code=resp_code.JWT_CREATE_ERROR, msg="JWT 信息生成异常")
    return comm_ret(resp={'jwt': jwt_str, 'refresh_jwt': refresh_jwt_str})


@user_router.route("/logout", methods=['GET'])
def logout():
    """
    登出
    """
    # jwt 做 用户认证 时，不存在可以注销的说法
    return comm_ret(code=resp_code.USER_LOGOUT, msg="用户登出", resp=g.user_info)
