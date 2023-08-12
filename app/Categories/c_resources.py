from flask.views import MethodView
from flask import Blueprint, request

Categories_blueprint = Blueprint("categories_blueprint", __name__, url_prefix='/api/')

class Categories(MethodView):
    def get(self):
        return {'message': "Categories"}
        

class Categories_id(MethodView):
    def get(self):
        data = request.get_json()
        id = data.get('id')
        if id is None:
            return{"message":"No hay id"},400
        return {id}
        
         
Categories_blueprint.add_url_rule(
    'categories',
    view_func=Categories.as_view("categories")
)   

Categories_blueprint.add_url_rule(
    'categories',
    view_func=Categories_id.as_view("id")
)
    