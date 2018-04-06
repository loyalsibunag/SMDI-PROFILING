import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'miss-you-tine'

    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/smdiprofiling'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 10