import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser() #parses the JSON payload. (POST/PUT)
    parser.add_argument('username', type=str, required=True, help='This field can not be left blank')#JSON must have 'price' field. (POST/PUT)
    parser.add_argument('password', type=str, required=True, help='This field can not be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel(data['username'], data['password']) #(**data)
        if user.find_by_username(data['username']):
            return {'message': 'User already exists'}

        else:
            user.save_to_db()
            return {'message': 'User successfully created'}, 201
