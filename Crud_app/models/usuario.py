import json



class Usuario:
    def __init__(self, email, senha, nome, Id):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.Id = Id
       


    def to_map(self):
        return {
            'Email': self.email,
            'Nome': self.nome
            
        }

    @staticmethod
    def from_map(map_data):
        email = map_data.get('Email')
        senha = map_data.get('Senha')
        nome = map_data.get('Nome')
        Id = map_data.get('Name')
 
        return Usuario(email, senha, nome, Id)

    def to_json(self):
        return json.dumps(self.to_map())

    @staticmethod
    def from_json(json_data):
        return Usuario.from_map(json.loads(json_data))