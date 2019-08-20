#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File :  main.py
@Desc :  项目启动模块
'''

# The Python Standard Modules(Library) and Third Modules(Library)

# User-defined Modules
from app import app
from global_config import app_run_config


if __name__ == '__main__':
    app.run(
        host=app_run_config['HOST'],
        port=app_run_config['PORT'],
        debug=app_run_config['DEBUG']
    )
