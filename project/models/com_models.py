#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  com_models.py  
@Desc :  公共模型
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from pydantic import Schema
# User-defined Modules
from project.models.proj_base_model import ProjectBaseModel


class PaginationModel(ProjectBaseModel):
    """
    分页模型
    """
    start:int=Schema(..., type=int, gte=0)
    size:int=Schema(..., type=int, gt=0)
