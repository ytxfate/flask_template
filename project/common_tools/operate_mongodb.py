import pymongo

from global_config import MongoDB_config

class OperateMongodb:
    """
    MongoDB 数据库操作
    """
    def __init__(self):
        self.MongoDB_config = MongoDB_config
    
    def conn_mongodb(self):
        """
        连接 MongoDB 数据库
            return mongo_connection and mongo_database
        """
        if self.MongoDB_config['URL'] != '':
            conn = pymongo.MongoClient(host=self.MongoDB_config['URL'])
        else:
            conn = pymongo.MongoClient(host=self.MongoDB_config['HOST'], port=self.MongoDB_config['PORT'])
        db = conn.get_database(self.MongoDB_config['DEFAULT_DB'])
        if self.MongoDB_config['AUTH'] == True:
            db.authenticate(self.MongoDB_config['USERNAME'], self.MongoDB_config['PASSWORD'])
        return conn, db