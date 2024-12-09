import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    PORT = str(os.environ.get("DB_PORT"))
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE 
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_RECORD_QUERIES = True