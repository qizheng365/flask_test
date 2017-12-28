from . import mail
from flask_mail import Message
from flask import render_template,current_app
from threading import Thread
from manage import app

def send_email(to,subject,template,**kwargs):
	msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template+'.html', **kwargs)
	msg.html = render_template(template+'.html', **kwargs)
	thread = Thread(target=send_email_thread, args=[app,msg])
	thread.start()

def send_email_thread(app,msg):
	with app.app_context():
		mail.send(msg)