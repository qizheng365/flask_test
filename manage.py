import os
from app import create_app,db,mail
from app.models import User,Role
from flask_script import Shell,Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app("default")

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command("db", MigrateCommand)

def make_shell_context():
	return dict(app=app,db=db,User=User,Role=Role,mail=mail)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
	"for unittest"
	import unittest
	tests = unittest.TestLoader().discover("tests")
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
	manager.run()
