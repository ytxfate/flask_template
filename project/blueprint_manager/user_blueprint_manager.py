#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    蓝图管理模块
"""

from flask import Blueprint, request

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
