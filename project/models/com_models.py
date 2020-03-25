#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  com_models.py  
@Desc :  公共模型
'''

# The Python Standard Modules(Library) and Third Modules(Library)

# User-defined Modules
from project.models.proj_base_model import ProjectBaseModel


class PaginationModel(ProjectBaseModel):
    """
    分页模型
    """
    start:int=0
    size:int=10
