
postgresql = {'host': 'postgres',
              'port':'5432',
         'user': 'postgres',
         'passwd': '1',
         'db': 'postgres'}


import os

user = os.environ["POSTGRES_USER"]
pwd = os.environ["POSTGRES_PASSWORD"]
host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
db = os.environ["POSTGRES_DB"]

postgresqlConfig = "postgresql://{}:{}@{}:{}/{}".format(user, pwd, host, port, db)