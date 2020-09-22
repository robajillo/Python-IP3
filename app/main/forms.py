from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,validators
from wtforms.validators import Required
from ..models import Pitch

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Enter the Title', validators=[Required()])
    category = SelectField('Category', choices=[('Business','Business'),('Job','Job'),('Promotion','Promotion')],validators=[Required()])
    pitch= TextAreaField('Write your Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write Your Comment Here..', validators=[Required()])
    submit = SubmitField('Submit Comments')