# -*- coding: utf-8 -*-
import bleach
import os
import redis
from dotenv import load_dotenv
os_env = os.environ
load_dotenv()

def uia_username_mapper(identity):
    # we allow pretty much anything - but we bleach it.
    return bleach.clean(identity, strip=True)


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY', '3nF3Rn0')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG_TB_ENABLED = os.environ.get('DEBUG_TB_ENABLED')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///enferno.sqlite3'
    # for postgres
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql:///enferno')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/2')
    result_backend = os.environ.get('result_backend', 'redis://localhost:6379/3')

    # security
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_CHANGEABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', '3nF3Rn0')
    SECURITY_USER_IDENTITY_ATTRIBUTES = [{"username": {"mapper": uia_username_mapper, "case_insensitive": True}},]
    SECURITY_USERNAME_ENABLE = True


    SECURITY_POST_LOGIN_VIEW = '/dashboard'
    SECURITY_POST_CONFIRM_VIEW = '/dashboard'
    SECURITY_POST_REGISTER_VIEW = '/login'

    SESSION_TYPE = 'redis'

    SESSION_REDIS = redis.from_url(os.environ.get('REDIS_SESSION', 'redis://localhost:6379/1'))
    PERMANENT_SESSION_LIFETIME = 3600

    # flask mail settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SECURITY_EMAIL_SENDER = os.environ.get('SECURITY_EMAIL_SENDER', 'info@domain.com')
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
