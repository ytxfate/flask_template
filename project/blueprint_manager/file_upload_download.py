#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    蓝图管理模块
"""

from flask import Blueprint, request

from project.modules.file_upload_download.file_upload import FileUpload
from project.modules.file_upload_download.file_download import FileDownload
from project.common_tools.operate_mongodb import OperateMongodb
from project.common_tools.operate_redis import OperateRedis

conn_mongo, db_mongo = OperateMongodb().conn_mongodb()
conn_redis = OperateRedis().conn_redis()

file = Blueprint("file", __name__)

# 文件上传
@file.route('/upload', methods=["POST"])
def file_upload():
    return FileUpload(request).upload_file()

# 文件下载
@file.route('/download', methods=["POST"])
def file_download():
    return FileDownload(request).download_file()

# 文件下载 -- 二进制流
@file.route('/download_stream', methods=["POST"])
def file_download_stream():
    return FileDownload(request).download_file_use_stream()
