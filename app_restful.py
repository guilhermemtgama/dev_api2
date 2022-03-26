from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades  import Habilidades

app = Flask (__name__)
api = Api (app)

desenvolverdores = [

    {'ID': '0',
     'nome': 'Guilherme',
     'habilidades': ['Python, Flask']
     },
    {'ID': '1',
     'nome': 'Leticia',
     'habilidades': ["Python", 'Django']}
]
# devolve um desenvolvedor pelo ID,também altera e deleta um desenvolvedor.

class Desenvolvedor (Resource,):
    def get(self,id):
        try:
            response = desenvolverdores[id]
        except IndexError:
            mensagem = 'Desenvolverdor de ID {} não existe'.format(id)
            response = {'status ': 'erro', 'mensagem ': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o adm da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return(response)

    def put(self, id):
        dados = json.loads(request.data)
        desenvolverdores[id] = dados
        return dados


    def delete(self,id):
        desenvolverdores.pop(id)
        return ({'Status': 'Sucesso', 'Mensagem': 'Registro excluido' })

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolverdores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolverdores)
        dados['id'] = posicao
        desenvolverdores.append(dados)
        return desenvolverdores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
if __name__ == '__main__':
    app.run(debug = True)