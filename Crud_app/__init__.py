from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
from Crud_app.routes import usuario  # Importe as rotas após criar a instância do Flask
