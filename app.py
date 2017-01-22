from flask import Flask,redirect
from database import db
from models import User, Role
from flask_security import Security, SQLAlchemyUserDatastore
from  security_forms import ExtendedRegisterForm
from flask_security.utils import url_for_security

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'


# 不发送注册信息到邮箱
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

# 有了这句你才可以自定义模板文件 要不然不成功的
app.config['SECURITY_REGISTERABLE'] = True

#注册db
db.init_app(app)

# 这个对象有好多功能可以用的
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

# Finalmente inicializa o package security passando contexto de aplicacao e instancia de "banco"
# 传输三个参数给security 第一个是app 第二个是user_datatstore 第三个是自定义的表单
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

@app.route('/')
def home():
    return redirect(url_for_security('register'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()