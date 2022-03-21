import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask('reactiveForms', instance_relative_config = True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
jwt = JWTManager(app)
db = SQLAlchemy(app)
api = Api(app)
CORS(app)

from angularForms.controller.register import Register
from angularForms.controller.user import GetList
from angularForms.controller.login import Login
# from angularForms.controller.logout import Logout

api.add_resource(Register, '/api/register')
api.add_resource(Login, '/api/login')
api.add_resource(GetList, '/api/listOfAccount')
# api.add_resource(Logout, '/logout')


# db.create_all()
# it is need for the relationship of the tables



