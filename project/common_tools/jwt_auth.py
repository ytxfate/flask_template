#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File :  jwt_auth.py
@Desc :  JWT 编码、解码
'''

# The Python Standard Modules(Library) and Third Modules(Library)
import datetime
import time
import jwt
import hashlib

# User-defined Modules
from global_config import SECRET_KEY as flask_secret_key


class JWTAuth:
    """
    JSON Web Token 用户认证
    """
    def __init__(self):
        # 对 falsk secret_key 进行二次处理，用于 jwt 加密
        self.secret_key = self.encrypt_md5(flask_secret_key)
    
    def encrypt_md5(self, encrypt_str):
        """
        md5 加密
            @param:
                encrypt_str: 需要加密的字符串(str)或字节码(bytes)
            @return:
                返回一个32位加密后的字符串
        """
        if isinstance(encrypt_str, str):
            # 如果是 unicode 先转 utf-8
            encrypt_str = encrypt_str.encode("utf-8")
        m = hashlib.md5()
        m.update(encrypt_str)
        return m.hexdigest()

    def encode_jwt(self, user_info, validity_period=30):
        """
        生成 jwt 认证信息
            :param user_info 必须包含以下字段
                [ user_id, username ]
            :param validity_period 
                jwt 有效期，默认 30 分钟
            
            :return: jwt 字串

            :rtype: str
        """
        jwt_body = ''
        payload_need_key = ['user_id', 'username']
        try:
            if set(user_info.keys()) == set(payload_need_key):
                payload = {
                    'exp': time.mktime((datetime.datetime.now() + datetime.timedelta(minutes=validity_period)).timetuple()),    # 过期时间
                    'iat': time.mktime(datetime.datetime.now().timetuple()),     # 发行时间
                    'iss': 'ken',       # token签发者
                    'data': {       # 数据(自行添加)
                        'user_id': user_info['user_id'],
                        'username': user_info['username']
                    }
                }
                jwt_body = jwt.encode(payload, self.secret_key, algorithm='HS256').decode(encoding='utf-8')
        except Exception as e:
            pass
        return jwt_body
    
    def decode_jwt(self, jwt_body):
        """
        解析 jwt 认证信息
            :param jwt_body
                jwt 字串
            
            :return: jwt 字串中的用户信息
                当 key jwt_status 为 T 时，解析成功；否则解析失败
            
            :rtype: dict
        """
        user_info = {'jwt_status': 'F'}
        try:
            jwt_payload = jwt.decode(jwt_body.encode(encoding='utf-8'), self.secret_key, options={'verify_exp': True})
            if jwt_payload and 'data' in jwt_payload:
                user_info = jwt_payload['data']
                user_info['jwt_status'] = 'T'
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
            pass
        return user_info
