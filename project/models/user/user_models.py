#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  user_models.py  
@Desc :  用户模型
'''

# Standard library imports

# Third party imports
from pydantic import constr
# Local application imports
from project.models.proj_base_model import ProjectBaseModel


class LoginInfoModel(ProjectBaseModel):
    """
    用户登录模型
    """
    username: constr(strip_whitespace=True, min_length=6)
    password: constr(strip_whitespace=True, min_length=6)


class RefreshJWTModel(ProjectBaseModel):
    """
    刷新 JWT 信息
    """
    jwt: constr(strip_whitespace=True, min_length=1)
    refresh_jwt: constr(strip_whitespace=True, min_length=1)
