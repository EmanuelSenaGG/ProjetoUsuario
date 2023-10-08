import requests, json
from Crud_app.models.Db import uri_create_user
from config import auth

dado = {
    "Nome": "Carlos",
    "Email": "Carlos234@gmail.com",
    "Senha": "778899"
    }

body = json.dumps(dado)
#req =requests.post(uri_create_user,data=body)

def cadastrar():
    try:
        auth.create_user_with_email_and_password(email = 'carlos234@gmail.com', password = '778899')
        request = requests.post(uri_create_user,body)
        return print('True')
    except:
        print('Ja existe usuario com essa conta')

def login():
    try:
        auth.sign_in_with_email_and_password(email = 'joao@gmail.com', password='123456789')
        return print('True')
    except:
        print('Usuario ou senha incorreto')

cadastrar()       
#login()