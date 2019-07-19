from flask import jsonify


def common_return(code=200, isSuccess=True, msg="请求成功", resp={}):
    """
    接口统一返回模板
        Args:
            code:       http状态码     int      默认 200
            isSuccess:  请求成功状态    bool    默认 True
            msg:        描述            str     默认 请求成功
            resp:       返回的数据结果集  object 默认 {}
        Returns:
            return jsonify
    """
    ret_json = {
        "code": code,
        "isSuccess": isSuccess,
        "msg": msg,
        "response": resp
    }
    return jsonify(ret_json)
