#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    主运行脚本
"""

from app import app
from global_config import app_run_config

app.run(
    host=app_run_config['HOST'],
    port=app_run_config['PORT'],
    debug=app_run_config['DEBUG']
)