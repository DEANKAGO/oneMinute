import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class config(object):
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  DEBUG = os.getenv('DEBUG')