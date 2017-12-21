from flask import render_template,url_for,redirect,session,flash
from datetime import datetime
from flask_login import login_required

from . import main
from ..forms import NameForm
from .. import db
from ..models import User

@main.route("/", methods=['GET','POST'])
def index():
	return render_template("Index.html")
#	user_agent = request.headers["User-Agent"]
#	form = NameForm()
#	if form.validate_on_submit():
#		user = User.query.filter_by(username=form.name.data).first()
#		if user is None:
#			db.session.add(User(username=form.name.data))
#			session["known"] = False
#			send_mail(user)
#		else:
#			session["known"] = True
#		old_name = session.get('name')
#		if form.name.data != old_name and old_name is not None:
#			flash("current name %s is diff from last name %s" % (form.name.data,old_name))
#		session['name'] = form.name.data
#		form.name.data=''
#		return redirect(url_for(".index"))
#	return render_template("Index.html", name=session.get('name'), form=form, known=session.get('known'), current_time=datetime.utcnow())


@main.route("/user/<username>")
def hello(username):
	return render_template("user.html", name=username)

@main.route("/secret")
@login_required
def secret():
	return "<h1>Hello, This is a secret page, only allowed for auth users</h1>"
