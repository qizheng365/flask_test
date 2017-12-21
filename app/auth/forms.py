from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Email,Length,EqualTo,Regexp
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
	email = StringField("Enter your email", validators=[Required(),Length(1,64),Email()])
	password = PasswordField("Enter your password", validators=[Required()])
	remember_me = BooleanField("Keep me in mind")
	submit = SubmitField('LogIn')

class RegisterForm(FlaskForm):
	email = StringField("Email", validators=[Required(),Length(1,64),Email()])
	username = StringField("Username", validators=[Required(), Length(1,64)])
	password = PasswordField("Password", validators=[Required()])
	password_confirm = PasswordField("Password Confirm", validators=[Required(), EqualTo("password", message='Must match Password')])
	submit = SubmitField('Register')

	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError("Email %s already registered!" % field.data)
			
	def validate_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError("username %s already in user!" % field.data)
	