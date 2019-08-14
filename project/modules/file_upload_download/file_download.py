#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import jsonify, send_from_directory, send_file
import os
import csv
import io

# 下载文件存储路径
DOWNLOAD_FILE_PATH = "./file/download/"


class FileDownload:
    def __init__(self, request):
        self.request = request
    
    def download_file(self):
        ret_obj = {"DownloadStatus": "false"}
        if self.request.json and 'file_name' in self.request.json and self.request.json['file_name']:
            # 判断文件是否存在
            if os.path.isfile(os.path.join(DOWNLOAD_FILE_PATH, self.request.json['file_name'])):
                return send_from_directory(DOWNLOAD_FILE_PATH, self.request.json['file_name'], as_attachment=True)
            else:
                ret_obj = {"DownloadStatus": "false", 'msg': 'no such file!'}
        else:
            ret_obj = {"DownloadStatus": "false", 'msg': 'no such file!'}
        return jsonify(ret_obj)
    
    def download_file_use_stream(self):
        csv_data = [
            ['name', 'sex', 'birthday'],
            ['user', 'boy', '2019-01-01']
        ]
        # 创建一个 io 流
        io_stream = io.StringIO()
        writer = csv.writer(io_stream)
        for row in csv_data:
            writer.writerow(row)
        mem = io.BytesIO()
        mem.write(io_stream.getvalue().encode('utf-8'))
        # Change stream position
        mem.seek(0)
        io_stream.close()
        return send_file(mem, as_attachment=True, attachment_filename='年度计划.csv', mimetype='text/csv')
