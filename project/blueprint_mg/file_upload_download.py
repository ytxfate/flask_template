#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  file_upload_download.py
@Desc :  文件上传下载蓝图管理模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from flask import Blueprint

# User-defined Modules
from project.modules.file_upload_download.file_download import FileDownload
from project.modules.file_upload_download.file_upload import FileUpload


file = Blueprint("file", __name__)

# 文件上传
@file.route('/upload', methods=["POST"])
def file_upload():
    return FileUpload().upload_file()

# 文件下载
@file.route('/download', methods=["POST"])
def file_download():
    return FileDownload().download_file()

# 文件下载 -- 二进制流
@file.route('/download_stream', methods=["POST"])
def file_download_stream():
    return FileDownload().download_file_use_stream()
