# -*- encoding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TableForm(Form):
    name = StringField(u'名字', validators=[DataRequired(), Length(1, 10)])
    department = StringField(u'部门', validators=[DataRequired(), Length(1.10)])
    year = StringField(u'年', validators=[DataRequired(), Length(1, 4)])
    month = StringField(u'月', validators=[DataRequired(), Length(1, 2)])
    day = StringField(u'日', validators=[DataRequired(), Length(1, 2)])
    days = StringField(u'预计天数', validators=[DataRequired(), Length(1, 4)])
    reason = StringField(u'出差事项', validators=[DataRequired(), Length(1, 100)])
    destination = StringField(u'目的地', validators=[DataRequired(), Length(1, 10)])
    manager = StringField(u'审核人', validators=[DataRequired(), Length(1,10)])
    boss = StringField(u'批准人', validators=[DataRequired(), Length(1,10)])
    submit = SubmitField(u'生成图片')
