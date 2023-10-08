from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# Configurar o CORS com opções adicionais
CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=["GET", "POST"], allow_headers=["Content-Type"])

from Crud_app.routes import usuario  # Importe as rotas após criar a instância do Flask
