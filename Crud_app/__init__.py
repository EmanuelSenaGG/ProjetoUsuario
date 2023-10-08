from flask import Flask

app = Flask(__name__)

from Crud_app.routes import usuario  # Importe as rotas após criar a instância do Flask
