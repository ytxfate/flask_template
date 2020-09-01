#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  main.py  
@Desc :  项目启动模块
'''

# Standard library imports

# Third party imports

# Local application imports
from project.app import app
from project.config.sys_config import app_run_conf, isFormalSystem


def main_run():
    debug_value = app_run_conf['DEBUG']
    # 判断是否为生产系统，若不是则开启 debug 功能
    if isFormalSystem:
        debug_value = False
    app.run(host=app_run_conf['HOST'],
            port=app_run_conf['PORT'],
            debug=debug_value)


if __name__ == '__main__':
    main_run()
