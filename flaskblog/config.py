import os


class Config:
    SECRET_KEY = 'c0352ded7a48343553fa964e2791973'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASS = os.environ.get('EMAIL_PASS')
