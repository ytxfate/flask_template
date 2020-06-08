#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  com_models.py  
@Desc :  公共模型
'''

# The Python Standard Modules(Library) and Third Modules(Library)
from pydantic import conint
# User-defined Modules
from project.models.proj_base_model import ProjectBaseModel


class PaginationModel(ProjectBaseModel):
    """
    分页模型
    """
    start:conint(ge=0)=0
    size:conint(gt=0)=10
