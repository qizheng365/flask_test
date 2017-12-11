#-*- encoding=utf-8 -*-

from flask import Flask,request,render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def main():
	user_agent = request.headers["User-Agent"]
	return render_template("main.html", agent=user_agent)

@app.route("/user/<username>")
def hello(username):
	mydict = {"user":username,"a":"b"}
	return render_template("user.html", dict_v=mydict),400

if __name__ == "__main__":
	manager.run()
	