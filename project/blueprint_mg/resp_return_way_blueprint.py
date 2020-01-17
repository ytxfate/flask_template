#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  resp_return_way_blueprint.py
@Desc :  response 返回方式 蓝图管理
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import Blueprint, request

# User-defined Modules
from project.modules.resp_return_way.resp_return_way import RespReturnWay

resp_return_way = Blueprint('resp_return_way', __name__)

@resp_return_way.route('use_jsonify', methods=['GET', 'POST'])
def resp_return_way_use_jsonify():
    return RespReturnWay(request).use_jsonify()

@resp_return_way.route('use_make_response', methods=['GET', 'POST'])
def resp_return_way_use_make_response():
    return RespReturnWay(request).use_make_response()

@resp_return_way.route('use_response', methods=['GET', 'POST'])
def resp_return_way_use_response():
    return RespReturnWay(request).use_response()
