from angularForms.app import app, db
from flask import Flask, request
from flask_restful import Resource, marshal_with
from angularForms.models.account import Account
from angularForms.parsing_formatting.register_parsing_arguments import get_Person
from flask_jwt_extended import (
	get_jwt_identity, get_jwt, jwt_required, unset_jwt_cookies
)

class GetList(Resource):
	@jwt_required(refresh=True)
	@marshal_with(get_Person)
	def get(self):
		
		get_all = Account.query.all()

		if request.method == 'GET':
			return get_all, 200












