from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField
from wtforms.validators import DataRequired,Length,Email
class ContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired(),Length(min=3,max=20)])
    email=EmailField("Email",validators=[DataRequired(),Email()])
    submit=SubmitField("Submit")