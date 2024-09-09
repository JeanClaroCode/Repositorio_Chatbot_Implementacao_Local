from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from dotenv import load_dotenv
import os

# Inicialize o carregamento de variáveis de ambiente do arquivo .env
load_dotenv()

db = SQLAlchemy()  # Inicialize o SQLAlchemy fora da função para uso global

def create_app():
    app = Flask(__name__, template_folder='../templates')

    swagger = Swagger(app)

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:!Ak34ncs.m@ec2-54-232-63-26.sa-east-1.compute.amazonaws.com/db_123_ajuda'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Inicialize o banco de dados com o app

    # Importação tardia para evitar importação cíclica
    with app.app_context():
        from app.routes import bp
        app.register_blueprint(bp)  # Registrar na raiz, sem o url_prefix

    return app  # Retorne o app criado

# A função register_blueprints foi incorporada diretamente dentro da função create_app(),
# então você pode removê-la completamente para evitar duplicação.
