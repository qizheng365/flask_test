from flask import Flask,request,render_template,url_for,redirect,session,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms import validators
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell,Manager
from flask_migrate import Migrate,MigrateCommand
from flask_mail import Mail,Message
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)
mail = Mail(app)

app.config['SECRET_KEY'] = "qizheng haha"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager.add_command("db", MigrateCommand)

#app.config["MAIL_SERVER"] = "smtp.qq.com"
#app.config["MAIL_PORT"] = 25
#app.config["MAIL_USE_TLS"] = True
#app.config["MAIL_USE_SSL"] = False
#app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
#app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
#app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
#app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <494925107@qq.com>'
#app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

def send_mail(user):
	msg = Message("Subject",sender="qzqz365@126.com",recipients=["494925107@qq.com"])
	msg.body = "%s registers on your web!" % user
	msg.html = "<html><head><title>Warning!</title></head><body><h1>Hello, Shit!</h1></body></html>"
	mail.send(msg)

def make_shell_context():
	return dict(app=app,db=db,User=User,Role=Role,mail=mail)

manager.add_command("shell", Shell(make_context=make_shell_context))

class User(db.Model):
	__tablename__="users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(10), unique=True)
	password = db.Column(db.Text, unique=True)
	role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
	def __repr__(self):
		return "name: %s, id: %s, role_id: %s" % (self.username, self.id,self.role_id)

class Role(db.Model):
	__tablename__ = "roles"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10), unique=True)
	users = db.relationship('User', backref="role", lazy="dynamic")
	def __repr__(self):
		return "name: %s, id: %s" % (self.name,self.id)

class RegisterForm(FlaskForm):
	name = StringField("Enter your name", validators=[validators.InputRequired(),validators.Length(min=4,max=10)])
#	email = StringField("Enter your email", validators=[validators.DataRequired(),validators.Length(min=4,max=10)])
#	password = PasswordField("Enter your password", validators=[validators.DataRequired(),validators.Length(min=4,max=10)])
#	confirm = PasswordField("Repeat Password", [validators.EqualTo("password", message="must match password")])
	submit = SubmitField('Submit')

@app.route("/", methods=['GET','POST'])
def main():
#	user_agent = request.headers["User-Agent"]
#	return render_template("main.html", agent=user_agent)
#	return render_template("main.html", current_time=datetime.utcnow())
	form = RegisterForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			db.session.add(User(username=form.name.data))
			session["known"] = False
			send_mail(user)
		else:
			session["known"] = True
#		old_name = session.get('name')
#		if form.name.data != old_name and old_name is not None:
#			flash("current name %s is diff from last name %s" % (form.name.data,old_name))
		session['name'] = form.name.data
		form.name.data=''
		return redirect(url_for("main"))
	return render_template("main.html", name=session.get('name'), form=form, known=session.get('known'))

@app.route("/user/<username>")
def hello(username):
	return render_template("user_bstrap.html", name=username)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template("500.html"),500

@app.route("/page")
def page():
	return url_for("static", filename="Wallpaper.bmp", _external=True)

if __name__ == "__main__":
	manager.run()
	