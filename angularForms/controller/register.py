from angularForms.app import app, db 
from flask import Flask, request, jsonify
from flask_restful import Resource, abort, marshal_with
from angularForms.models.account import Account
from angularForms.models.address import Address
from angularForms.parsing_formatting.register_parsing_arguments import signUp_parser, signUp_fields
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class Register(Resource):
	@marshal_with(signUp_fields)

	def post(self):

		check_first = request.json.get("username", None)

		username_taken = Account.query.filter_by(username= check_first).first()

		if username_taken:
			return abort(400, message="Username is already taken")

		signUp_args = signUp_parser.parse_args(strict=True)

		if request.method == 'POST':

			hashed_password = generate_password_hash(
				signUp_args['password'],
				method='sha512'
			)

			if hashed_password:

				sign_up = Account(
					public_id=str(uuid.uuid4()),
					firstName=signUp_args['firstName'],
					lastName=signUp_args['lastName'],
					username=signUp_args['username'],

					password=hashed_password
				)

				address = Address(
					street=signUp_args['street'],
					city=signUp_args['city'],
					state=signUp_args['state'],
					zipCode=signUp_args['zipCode']
				)

				sign_up.address = address

				sign_up.add_db_account()

				return sign_up, 201





















