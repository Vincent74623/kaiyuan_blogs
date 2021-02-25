from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class ArtcleForm(FlaskForm):
    body_title = StringField('标题',validators=[DataRequired()])
    body_fenlei = StringField('分类',validators=[DataRequired()])
    body_url = StringField('封面图片url',validators=[DataRequired()])
    body = TextAreaField('正文',id='content')
    submit = SubmitField('发表')