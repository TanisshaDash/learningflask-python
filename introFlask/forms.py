from flask_wtf import FlaskForm  # Correct import for FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):  
    name = StringField("Candidate Name", [DataRequired(message="Please enter your name.")])  
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])  
    Address = TextAreaField("Address")  
    
    email = StringField("Email", [
        DataRequired(message="Please enter your email address."),
        Email(message="Please enter a valid email address.")
    ])  
    
    Age = IntegerField("Age")  
    language = SelectField('Programming Languages', choices=[('java', 'Java'), ('py', 'Python')])  
    
    submit = SubmitField("Submit")