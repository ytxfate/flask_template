#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import jsonify
from werkzeug.utils import secure_filename
import os
import time

# 上传文件存储路径
UPLOAD_FILE_PATH = "./file/upload/"

class FileUpload:
    def __init__(self, request):
        self.request = request
    
    def upload_file(self):
        """
        下载文件
        """
        ret_obj = {"UploadStatus": "false"}
        file = self.request.files.get("file")
        if file and file.filename != "":
            # 使用 secure_filename 格式化文件名称
            file_name = secure_filename(file.filename)
            # 获取文件的后缀名
            file_end_with = file_name.rsplit(".")[1]
            # 为上传的文件创建新的文件名
            new_filename = str(int(time.time() * 1000)) + "." + file_end_with
            # 保存文件
            file.save(os.path.join(UPLOAD_FILE_PATH, new_filename))
            ret_obj = {"UploadStatus": "true", "file_name": new_filename}
        else:
            ret_obj = {"UploadStatus": "false", "msg": "no file upload!"} 
        return jsonify(ret_obj)
