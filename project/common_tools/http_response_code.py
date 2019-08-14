#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# ===================  基本 HTTP response code  =================== #
SUCCESS = 200                           # 成功
EXCEPTION_ERROR = 400                   # 异常错误

# ===================  其他 HTTP response code  =================== #
PARAMETER_ERROR = 1000                  # 参数异常错误
DATA_CHECK_ERROR = 1001                 # 数据比对出错(数据库中不存在此数据 或 此数据已存在于数据库中)
DATA_INSERT_ERROR = 1002                # 数据写入数据库出错
DATA_UPDATE_ERROR = 1003                # 数据库数据更新出错
DATA_DELETE_ERROR = 1004                # 数据库数据删除出错
DOCUMENTS_ARE_NOT_SUPPORTED = 1005      # 不支持的文件上传格式
FILE_NOT_FOUND = 1006                   # 文件不存在
