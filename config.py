postgresql = {'host': 'localhost',
              'port':'5433',
         'user': 'postgres',
         'passwd': '1',
         'db': 'postgres'}

postgresqlConfig = "postgresql://{}:{}@{}:{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['port'],postgresql['db'])