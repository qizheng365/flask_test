from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms import validators

class NameForm(FlaskForm):
	name = StringField("Enter your name", validators=[validators.InputRequired(),validators.Length(min=4,max=10)])
#	email = StringField("Enter your email", validators=[validators.DataRequired(),validators.Length(min=4,max=10)])
#	password = PasswordField("Enter your password", validators=[validators.DataRequired(),validators.Length(min=4,max=10)])
#	confirm = PasswordField("Repeat Password", [validators.EqualTo("password", message="must match password")])
	submit = SubmitField('Submit')