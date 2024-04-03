from flask import Flask, render_template, request
from models import Clientes, db


class Myserver():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/apiflash3190'
        db.init_app(self.app)        
        self.defaults_routes()


    def run(self):
        self.app.run(port=3000, debug=True, host='localhost')

    def home(self):
        user = Clientes("Carlos", "suamamis")
        return render_template('home.html', user=user)

    def clientes(self):
        if request.method == 'POST':
            try:
                data = request.get_json()
            
                user = Clientes(data['nome'], data['senha'])
                db.session.add(user)
                db.session.commit()

                return 'Usuario criado com sucesso', 200
            except Exception as e:
                return 'O usuário não foi criado. Erro: {}'.format(str(e)), 405
        elif request.method == 'GET':      
            try:
                data = Clientes.query.all()
                print([cliente.to_dict() for cliente in data])
                return render_template('clientes.html', data={'clientes':[cliente.to_dict() for cliente in data]})

            except Exception as e:
                return "O usuário não foi encontrado. Erro: {}".format(str(e)), 405



    def defaults_routes(self):
        self.app.route("/")(self.home)
        self.app.route("/clientes", methods=['POST', 'GET'])(self.clientes)





app = Myserver()
app.run()