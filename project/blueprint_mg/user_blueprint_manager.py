#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  user_blueprint_manager.py
@Desc :  用户蓝图管理模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import Blueprint

# User-defined Modules
from project.modules.user.user import UserModul

user = Blueprint("user", __name__)


@user.route('/login', methods=["POST"])
def user_login():
    return UserModul().login()


@user.route('/refresh_login_status', methods=["POST"])
def user_refresh_login_status():
    return UserModul().refresh_login_status()


@user.route("/logout", methods=['GET'])
def user_logout():
    return UserModul().logout()
