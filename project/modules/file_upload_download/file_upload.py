#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  file_upload.py  
@Desc :  文件上传模块
'''

# Standard library imports
import os
import time
# Third party imports
from flask import request, Blueprint
from pypinyin import lazy_pinyin
from werkzeug.utils import secure_filename
# Local application imports
from project.utils import resp_code
from project.utils.comm_ret import comm_ret


# 上传文件存储路径
UPLOAD_FILE_PATH = "./file/upload/"

upload_router = Blueprint("file_upload", __name__)


@upload_router.route('/upload', methods=["POST"])
def upload_file():
    """
    上传文件
    """
    file = request.files.get("file")
    if file and file.filename != "":
        # 使用 secure_filename 格式化文件名称
        # lazy_pinyin 用于解决中文文件名的文件
        file_name = secure_filename(''.join(lazy_pinyin(file.filename)))
        # 获取文件的后缀名
        file_end_with = file_name.rsplit(".")[1]
        # 为上传的文件创建新的文件名
        new_filename = str(int(time.time() * 1000)) + "." + file_end_with
        # 保存文件
        file.save(os.path.join(UPLOAD_FILE_PATH, new_filename))
        return comm_ret(msg='文件上传成功', resp={"file_name": new_filename})
    else:
        return comm_ret(msg='no file upload!')
