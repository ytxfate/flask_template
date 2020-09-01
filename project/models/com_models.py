#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  com_models.py  
@Desc :  公共模型
'''

# Standard library imports

# Third party imports
from pydantic import conint
# Local application imports
from project.models.proj_base_model import ProjectBaseModel


class PaginationModel(ProjectBaseModel):
    """
    分页模型
    """
    start:conint(ge=0)=0
    size:conint(gt=0)=10
