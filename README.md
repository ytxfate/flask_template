# flask_template
Flask 开发模板

###### 目录说明
```
|-- main.py             --> 项目启动文件
|-- app.py              --> 项目基本设置、蓝图全局注册、全局拦截器、全局异常处理等
|-- global_config.py    --> 全局配置文件
|-- project             --> 项目入口
    |-- blueprint_manager   --> 蓝图模块管理
        |-- user_blueprint_manager.py   --> user 模块蓝图管理（示例）
    |-- modules             --> 项目模块管理
        |-- user                        --> user 模块开发（示例）
            |-- user.py                     --> user 具体模块开发（示例）
    |-- common_tools        --> 其他常用工具（例如：数据库连接等）
        |-- operate_mongo.py                --> MongoDB 数据库操作（实例）
        |-- operate_redis.py                --> Redis 数据库操作（实例）
        |-- check_param_imp_keys.py         --> 检测请求参数
        |-- common_return.py                --> 统一 response 封装
        |-- http_response_code.py           --> response 状态码  （其他状态码可自行根据开发需要添加添加）
|-- file            --> 上传下载文件放置目录
    |-- download    --> 下载文件放置目录
    |-- upload      --> 上传文件放置目录
```


```
说明：示例部分可随项目的开发进行调整
```