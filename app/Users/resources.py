from flask.views import MethodView
from flask import Blueprint, request

users_blueprint = Blueprint("users_blueprint", __name__, url_prefix='/api/')

class UsersList(MethodView):
    def get(self):
        return {'message': "User list"}

class User(MethodView):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')
        if email is None:
            return{"message":"No has ingresado tu correo"},400
        if username is None:
            return{"message":"No has ingresado tu usuario"},400
        
         
users_blueprint.add_url_rule(
    'users',
    view_func=UsersList.as_view("users_list")
)   
    