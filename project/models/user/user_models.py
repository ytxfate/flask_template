#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  user_models.py  
@Desc :  用户模型
'''

# The Python Standard Modules(Library) and Third Modules(Library)

# User-defined Modules
from project.models.proj_base_model import ProjectBaseModel


class LoginInfoModel(ProjectBaseModel):
    """
    用户登录模型
    """
    username: str
    password: str

class RefreshJWTModel(ProjectBaseModel):
    """
    刷新 JWT 信息
    """
    jwt: str
    refresh_jwt: str
