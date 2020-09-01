#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  resp_return_way.py  
@Desc :  response 返回的方式
'''

# Standard library imports
import json
# Third party imports
from flask import jsonify, Response, make_response, Blueprint
import flask
# Local application imports


resp_return_way_router = Blueprint("resp_return_way", __name__)


@resp_return_way_router.route('/use_jsonify', methods=['GET', 'POST'])
def use_jsonify():
    return jsonify({'way': 'jsonify'})


@resp_return_way_router.route('/use_make_response', methods=['GET', 'POST'])
def use_make_response():
    # 自己封装 response
    resp = make_response(
        json.dumps({'way': "make_response"}, ensure_ascii=False))
    resp.status = "201"
    resp.headers["content-type"] = "application/json"
    resp.headers["Authorization"] = "jwt_str"
    return resp     # make_response 自己封装返回 json 格式数据，
                    # 可同时设置 headers 相关值


@resp_return_way_router.route('/use_response', methods=['GET', 'POST'])
def use_response():
    return Response(
        json.dumps({'way': "Response"}, ensure_ascii=False),
        mimetype='application/json'
    )   # Response 封装返回 json 格式数据
