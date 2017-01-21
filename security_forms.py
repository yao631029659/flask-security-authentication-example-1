from flask_security.forms import RegisterForm, StringField, Required

class ExtendedRegisterForm(RegisterForm):
    # 扩展了原来的RegistterForm 加了一个那么字段
    name = StringField('Name', [Required('Name not provided')])    