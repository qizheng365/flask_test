import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	SECRET_KEY = os.environ.get("SECRET_KEY") or "This is my secret key string"
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'qzqz365@126.com'
	FLASKY_ADMIN = '[Flasky Admin]'
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or "sqlite:///"+os.path.join(basedir, 'data-dev.sqlite')
	MAIL_SERVER = "smtp.126.com"
	MAIL_PORT = 25
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or "sqlite:///"+os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///"+os.path.join(basedir, 'data.sqlite')


config = {"development":DevelopmentConfig,"testing":TestingConfig,"production":ProductionConfig,"default":DevelopmentConfig}
