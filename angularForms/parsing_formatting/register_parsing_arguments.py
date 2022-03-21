from flask_restful import reqparse, fields

signUp_parser = reqparse.RequestParser()
signUp_parser.add_argument("firstName", type=str, help="First Name of the person is required", required=True)
signUp_parser.add_argument("lastName", type=str, help="Last Name of the person is required", required=True)
signUp_parser.add_argument("username", type=str, help="Username of the person is required", required=True)
signUp_parser.add_argument("password", type=str, help="Password of the person is required", required=True)
signUp_parser.add_argument("street", type=str, help="Street Name of the person is required", required=True)
signUp_parser.add_argument("city", type=str, help="City Name of the person is required", required=True)
signUp_parser.add_argument("state", type=str, help="State of the person is required", required=True)
signUp_parser.add_argument("zipCode", type=str, help="Zip Code of the person is required", required=True)



signUp_fields = {
	'firstName' : fields.String,
	'lastName' : fields.String,
	'username' : fields.String,
}

get_Person = {
	'firstName' : fields.String,
	'lastName' : fields.String,
	'username' : fields.String,
}

