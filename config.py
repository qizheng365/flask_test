import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	SECRET_KEY = os.environ.get("SECRET_KEY") or "This is my secret key string"
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <494925107@qq.com>'
	FLASKY_ADMIN = '[Flasky]'
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or "sqlite:///"+os.path.join(basedir, 'data-dev.sqlite')
	MAIL_SERVER = "smtp.qq.com"
	MAIL_PORT = 25
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_USERNAME = "494925107@qq.com"
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or "sqlite:///"+os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///"+os.path.join(basedir, 'data.sqlite')


config = {"development":DevelopmentConfig,"testing":TestingConfig,"production":ProductionConfig,"default":DevelopmentConfig}
