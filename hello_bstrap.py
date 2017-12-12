from flask import Flask,request,render_template,url_for,redirect,session,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField
from wtforms import validators
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = "qizheng haha"

#数据库sqlite连接
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class RegisterForm(Form):
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
		old_name = session.get('name')
		if form.name.data != old_name and old_name is not None:
			flash("current name %s is diff from last name %s" % (form.name.data,old_name))
		session['name'] = form.name.data
		form.name.data=''
		return redirect(url_for("main"))
	return render_template("main.html", name=session.get('name'), form=form)

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
	app.run()
	