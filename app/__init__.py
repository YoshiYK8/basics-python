from flask import Flask
from flask.views import MethodView
from .Users.resources import users_blueprint
from .Database import db

class HelloWorld(MethodView):
    def get(self):
        return {'message': "Prueba debug flask"}
    #def post(self):
        #Subir los cambios a la nube
    #def patch(self):
        #Reemplazar con cambios especificos en la nube
    #def delete(self):
        #Borrar cosas de la nube con datos especificos

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../settings.py')
    hello_world = HelloWorld.as_view("hello_world")
    app.add_url_rule('/', view_func=hello_world)
    app.add_url_rule('/api/', view_func = hello_world)
    app.register_blueprint(users_blueprint)

    return app  