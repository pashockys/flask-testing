import os
from pathlib import Path
basedir = os.path.abspath(os.path.dirname(__file__))
basedir2 = Path(__file__).resolve()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print("@#@#@#@#@#@", SQLALCHEMY_DATABASE_URI)




