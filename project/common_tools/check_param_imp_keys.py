#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def check_param_imp_keys(imp_key_set, req_dict):
    """
    检查必要参数是否不全或为空
    """
    if req_dict:
        for imp_key in imp_key_set:
            if imp_key in req_dict:
                if isinstance(req_dict[imp_key], str):
                    if req_dict[imp_key].strip() == '':
                        return False
                else:
                    if req_dict[imp_key] is None:
                        return False
            else:
                return False
    else:
        return False
    return True

def check_param_can_change_keys(can_change_keys, req_dict):
    """
    检查请求的所有参数是否都在允许修改的 keys 中
    """
    for key in req_dict.keys():
        if key not in can_change_keys:
            return False
    return True
