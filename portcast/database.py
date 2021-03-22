from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(
    str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'portcast')
db_username = urllib.parse.quote_plus(
    str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(
    str(os.environ.get('db_password', 'secret')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode', 'prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(
    db_username, db_password, host_server, db_server_port, database_name, ssl_mode)


engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

