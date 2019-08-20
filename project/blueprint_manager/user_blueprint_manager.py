#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File :  user_blueprint_manager.py
@Desc :  用户蓝图管理模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import Blueprint, request

# User-defined Modules
from project.modules.user.user import UserModul
from project.common_tools.operate_mongodb import OperateMongodb
from project.common_tools.operate_redis import OperateRedis


conn_mongo, db_mongo = OperateMongodb().conn_mongodb()
conn_redis = OperateRedis().conn_redis()

user = Blueprint("user", __name__)


@user.route('/login', methods=["GET", "POST"])
def user_login():
    return UserModul(request).login()


@user.route("/logout", methods=["GET",'POST'])
def user_logout():
    return UserModul(request).logout()
