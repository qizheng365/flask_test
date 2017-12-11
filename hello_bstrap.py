#-*- encoding=utf-8 -*-

from flask import Flask,request,render_template,url_for,redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def main():
#	user_agent = request.headers["User-Agent"]
#	return render_template("main.html", agent=user_agent)
	return render_template("main.html", current_time=datetime.utcnow())

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
	