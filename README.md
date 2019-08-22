# flask_template
Flask 开发模板

###### 目录说明
```
|-- main.py             --> 项目启动文件
|-- app.py              --> 项目基本设置、蓝图全局注册、全局拦截器、全局异常处理等
|-- global_config.py    --> 全局配置文件
|-- project             --> 项目入口
    |-- blueprint_manager   --> 蓝图模块管理
        |-- file_upload_download.py         --> 文件上传下载 模块蓝图管理（示例）
        |-- resp_return_way_blueprint.py    --> response 返回方式 模块蓝图管理（示例）
        |-- user_blueprint_manager.py       --> user 模块蓝图管理（示例）
    |-- modules                 --> 项目模块管理
        |-- user                    --> user 模块开发（示例）
            |-- user.py                 --> user 具体模块开发（示例）
        |-- file_upload_download    --> 文件模块（示例）
            |-- file_download.py        --> 文件下载模块（示例）
            |-- file_upload.py          --> 文件上传模块（示例）
        |-- resp_return_way         --> response 返回方式模块（示例）
            |-- resp_return_way.py      --> response 返回方式模块（示例）
    |-- common_tools                --> 其他常用工具（例如：数据库连接等）
        |-- operate_mongodb.py          --> MongoDB 数据库操作（实例）
        |-- operate_redis.py            --> Redis 数据库操作（实例）
        |-- check_and_handle_request_param.py   --> 检查及处理 request 请求参数
        |-- common_return.py            --> 统一 response 封装
        |-- http_response_code.py       --> response 状态码  （其他状态码可自行根据开发需要添加添加）
        |-- jwt_auth.py                 --> JWT 编码 及 解码
|-- file        --> 上传下载文件放置目录
    |-- download    --> 下载文件放置目录
    |-- upload      --> 上传文件放置目录
|-- uwsgi.ini   --> uwsgi 启动配置文件
```

```
说明：示例部分可随项目的开发进行调整
```

**uwsgi 配置说明(注意：实际部署中最好把注释去掉)**
```
http = 0.0.0.0:5000
plugin = python3        ; 使用插件-编程语言
chdir = /opt/flask/flask_template    ; 指定项目目录
processes = 4           ; 开启进程数量
threads = 2
enable-threads = true   ; 允许用内嵌的语言启动线程;这将允许你在app程序中产生一个子线程
max-requests = 8192     ; 设置每个进程请求数上限
master = true           ; 允许主线程存在
wsgi-file = ./main.py
callable = app
; home = ../venv      ; 虚拟环境目录
```

```
启动命令: uwsgi --ini uwsgin.ini
重启命令: uwsgi --reload uwsgi.pid
关闭命令: uwsgi --stop uwsgi.pid
实时状态: uwsgi --connect-and-read uwsgi/uwsgi.status
```
