#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File :  check_request_param.py
@Desc :  检查 request 请求参数
'''

# The Python Standard Modules(Library) and Third Modules(Library)

# User-defined Modules


def check_param_must_keys(must_key_collection, request_dict):
    """
    检查必要参数是否不全或为空
        @param:
            must_key_collection : api 接口函数必要的 request 参数
            request_dict        : request 请求的参数及值
        @retuen:
            return Boolean
            if return is False,the parameters is check fail,
            if return is True,the parameters is check success
    """
    if request_dict:
        for must_key in must_key_collection:
            if must_key in request_dict:
                # 参数类型为字符串时，值不能为空字符串
                if isinstance(request_dict[must_key], str):
                    if request_dict[must_key].strip() == '':
                        return False
                else:
                    if request_dict[must_key] is None:
                        return False
            else:
                return False
    else:
        return False
    return True


def check_param_can_change_keys(can_change_keys, request_dict):
    """
    检查请求的所有参数是否都在允许修改的 keys 中
        @param:
            can_change_keys : api 接口函数允许的 request 参数
            request_dict    : request 请求的参数及值
        @retuen:
            return Boolean
            if return is False,the parameters is check fail,
            if return is True,the parameters is check success
    """
    for key in request_dict.keys():
        if key not in can_change_keys:
            return False
    return True
