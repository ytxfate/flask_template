#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  __init__.py
@Desc :  蓝图管理模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)

# User-defined Modules
from ..app import app


root_url = '/api'   # 当服务器使用 nginx 做反向代理的时候
                    # 可修改 root_url 已便 nginx 拦截请求
                    # 若不需要可以设置为空

from .user_blueprint_manager import user
from .file_upload_download import file
from .resp_return_way_blueprint import resp_return_way
BLUEPRINT_LIST = [
    {"blueprint": user, "url_prefix": root_url + "/user"},
    {"blueprint": file, "url_prefix": root_url + "/file"},
    {"blueprint": resp_return_way, "url_prefix": root_url + "/resp_return_way"},
]
for bp in BLUEPRINT_LIST:
    app.register_blueprint(bp['blueprint'], url_prefix=bp['url_prefix'])
