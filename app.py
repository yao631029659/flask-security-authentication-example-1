from flask import Flask
from database import db
from models import User, Role
from flask_security import Security, SQLAlchemyUserDatastore
from  security_forms import ExtendedRegisterForm

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

# Configuracao para nao enviar email no registro de novos usuarios
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

# Necessario para habilitar o registro de novos usuarios
app.config['SECURITY_REGISTERABLE'] = True

# Inicializa a instancia do banco dentro do contexto da aplicacao
db.init_app(app)

# A classe SQLAlchemyUserDatastore implementa os metodos necessarios para CRUD de usuarios e permissoes
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

# Finalmente inicializa o package security passando contexto de aplicacao e instancia de "banco" 
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", debug=True, port=8080)