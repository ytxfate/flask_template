#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  blueprint_mg.py  
@Desc :  蓝图管理模块
'''

# Standard library imports

# Third party imports

# Local application imports
from project.app import app
from project.config.sys_config import prefix_api_path as root_url


""" 路由注册 """
from project.modules.file_upload_download.file_download import download_router as file_download_router
from project.modules.file_upload_download.file_upload import upload_router as file_upload_router
from project.modules.resp_return_way.resp_return_way import resp_return_way_router
from project.modules.user.user import user_router

BLUEPRINT_LIST = [
    {"blueprint": user_router, "url_prefix": "/user"},
    {"blueprint": file_download_router, "url_prefix": "/file"},
    {"blueprint": file_upload_router, "url_prefix": "/file"},
    {"blueprint": resp_return_way_router, "url_prefix": "/resp_return_way"},
]
for bp in BLUEPRINT_LIST:
    app.register_blueprint(
        bp['blueprint'],
        url_prefix=root_url + bp['url_prefix']
    )
