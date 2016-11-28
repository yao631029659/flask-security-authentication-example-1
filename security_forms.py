from flask_security.forms import RegisterForm, StringField, Required

class ExtendedRegisterForm(RegisterForm):
    name = StringField('Name', [Required('Name not provided')])    