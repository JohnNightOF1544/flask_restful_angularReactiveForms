from angularForms.app import app, db
from flask import Flask, request, make_response, url_for, render_template, jsonify
from flask_restful import Resource, abort, marshal_with
from angularForms.models.account import Account
from angularForms.parsing_formatting.login_parsing_arguments import login_parser, login_fields
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime
from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_jwt, 
    unset_jwt_cookies, set_access_cookies, JWTManager, jwt_required, set_refresh_cookies
)

class Login(Resource):

    def post(self):

        alias = request.json.get("username", None)
        password = request.json.get("password", None)

        valid_username = Account.query.filter_by(username=alias).first()

        if not valid_username:
            return {'message': 'Please input exact {} or {} correctly from username'.format('username', 'password')}

        check_pass = check_password_hash(valid_username.password, password)

        if not check_pass:
            return {'message': 'Please input {} or {} correctly from password'.format('username', 'password')}

        if request.method == 'POST':

            access_token = create_access_token(identity=valid_username, fresh = True)
            refresh_token = create_refresh_token(identity=valid_username)
            
            resp = jsonify({'access_token': access_token, 'refresh_token': refresh_token, 'Login': True})

            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)

            return resp






























































# from angularForms.app import app, db
# from flask import Flask, request, jsonify
# from angularForms.models.account import Account
# from flask_restful import Resource, abort, marshal_with
# from angularForms.parsing_formatting.login_parsing_arguments import login_parser, login_fields
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_jwt_extended import (
# 	create_access_token, create_refresh_token, get_jwt,
# 	unset_jwt_cookies, set_access_cookies, JWTManager, jwt_required, set_refresh_cookies
# )

# class Login(Resource):
# 	def post(self):
		
# 		alias = request.json.get("username", None)
# 		password = request.json.get("password", None)

# 		valid_username = Account.query.filter_by(username=alias).first()

# 		if not valid_username:
# 			return { 'message': 'Please input exact {} or {} correctly from input fields'.format('username', 'password')}

# 		valid_password = check_password_hash(valid_username.password, password)

# 		if not valid_password:
# 			return {'message': 'Please input {} or {} correctly from input fields'.format('username', 'password')}


# 		if request.method == 'POST':

# 			access_token = create_access_token(identity=valid_username, fresh = True)
# 			refresh_token = create_refresh_token(identity=valid_username)

# 			resp = jsonify({'access_token': access_token, 'refresh_token': refresh_token, 'Login': True})

# 			set_access_cookies(resp, access_token)
# 			set_refresh_cookies(resp, refresh_token)

# 			return resp












