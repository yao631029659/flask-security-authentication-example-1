from flask_security.forms import RegisterForm, StringField, Required

# 这些个字段 都是重flask_security里面弄来的，作者应该做了一些自定义
class ExtendedRegisterForm(RegisterForm):
    # 扩展了原来的RegistterForm 加了一个名称字段字段
    name = StringField('Name', [Required('Name not provided')])