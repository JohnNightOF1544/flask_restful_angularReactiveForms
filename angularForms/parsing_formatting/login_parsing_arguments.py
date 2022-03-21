from flask_restful import reqparse, fields

login_parser = reqparse.RequestParser()
login_parser.add_argument("username", type=str, help="Please input your name")
login_parser.add_argument("password", type=str, help="Please input your password")

login_fields = {
	'username': fields.String,
	'password': fields.String
}
















