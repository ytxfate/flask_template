import redis

from global_config import Redis_config
class OperateRedis:
    """
    操作 Redis 数据库
    """
    def __init__(self):
        self.Redis_config = Redis_config
    
    def conn_redis(self):
        """
        连接 Redis 数据库
        """
        if self.Redis_config['AUTH'] == True:
            pool = redis.ConnectionPool(
                host=self.Redis_config['HOST'],
                port=self.Redis_config['PORT']
            )
        else:
            pool = redis.ConnectionPool(
                host=self.Redis_config['HOST'],
                port=self.Redis_config['PORT'],
                password=self.Redis_config['PASSWORD'])
        conn = redis.Redis(connection_pool=pool, decode_responses=self.Redis_config['DECODE_RESPONSES'])
        return conn