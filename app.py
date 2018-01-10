from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.msgs import Msg, MsgsList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'anuj'
api = Api(app)

jwt = JWT(app, authenticate, identity) #JWT creates a new end point /auth

api.add_resource(Msg, '/msg/<int:mid>')
api.add_resource(MsgsList, '/messages')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
