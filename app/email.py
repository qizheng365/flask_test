from . import mail
from flask_mail import Message
from flask import render_template,current_app

def send_email(to,subject,template,**kwargs):
	msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,sender=current_app.config['FLASKY_MAIL_SENDER'],recipients=[to])
	msg.body = render_template(template+'.txt', **kwargs)
	msg.html = "<html><head><title>Confirm Your Account!</title></head></html>"
	mail.send(msg)
