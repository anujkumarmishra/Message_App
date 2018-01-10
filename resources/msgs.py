from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from flask_restful import Api
from models.msgs import MsgModel

#jwt = JWT(app, authenticate, identity)

class Msg(Resource):
    parser = reqparse.RequestParser() #parses the JSON payload. (POST/PUT)
    parser.add_argument('msg', type=str, required=True, help='This field can not be left blank')#JSON must have 'price' field. (POST/PUT)

    @jwt_required()
    def get(self, mid):
        message = MsgModel.find_by_mid(mid)
        if message:
            s = message.msg
            l = list(s.lower())
            if l[::] == l[::-1]:
                return {'message': message.json(), 'alert': 'It is a palindrome'}
            else:
                return message.json()

        else:
            return {'alert': 'Message not found'}, 404


    def post(self, mid):
        if MsgModel.find_by_mid(mid):
            return {'alert':'A message with mid {x} already exists'.format(x=mid)}, 400
        else:
            data = Msg.parser.parse_args()
            message = MsgModel(mid, data['msg'])
            try:
                message.save_to_db()
            except:
                return {'alert': 'An error occurred'}, 500 #Internal server error
            return message.json(), 201

    def delete(self, mid):
        message = MsgModel.find_by_mid(mid)
        if message:
            message.delete_from_db()
            return {'alert': 'Message deleted'}
        else:
            return {'alert': 'Message not found'}


    def put(self, mid):
        data = Msg.parser.parse_args()
        message = MsgModel.find_by_mid(mid)
        if message:
            message.msg = data['msg']
        else:
            message = MsgModel(mid, data['msg'])
        message.save_to_db()
        return message.json()

class MsgsList(Resource):
    def get(self):
        return {'messages': [message.json() for message in MsgModel.query.all()]}
