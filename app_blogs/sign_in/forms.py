from wtforms.validators import DataRequired
from wtforms import SubmitField,StringField,PasswordField
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])
    submit = SubmitField('登录')