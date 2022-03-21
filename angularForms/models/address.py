from angularForms.app import db

class Address(db.Model):
	__tablename__="address"
	id = db.Column(db.Integer, primary_key=True)
	street = db.Column(db.String(255), nullable=False)
	city = db.Column(db.String(100), nullable=False)
	state = db.Column(db.String(255), nullable=False)
	zipCode = db.Column(db.String(7), nullable=False)

	def __init__(self, street, city, state, zipCode):
		self.street = street
		self.city = city
		self.state = state
		self.zipCode = zipCode



