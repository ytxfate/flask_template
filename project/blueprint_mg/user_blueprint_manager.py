#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  user_blueprint_manager.py
@Desc :  用户蓝图管理模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import Blueprint, request

# User-defined Modules
from ..modules.user.user import UserModul

user = Blueprint("user", __name__)


@user.route('/login', methods=["POST"])
def user_login():
    return UserModul(request).login()


@user.route('/refresh_login_status', methods=["POST"])
def user_refresh_login_status():
    return UserModul(request).refresh_login_status()


@user.route("/logout", methods=['GET'])
def user_logout():
    return UserModul(request).logout()