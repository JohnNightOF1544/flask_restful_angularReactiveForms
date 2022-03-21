from angularForms.app import db, jwt
from sqlalchemy import ForeignKey

class Account(db.Model):
	__tablename__="account"
	id = db.Column(db.Integer, primary_key = True)
	public_id = db.Column(db.String(100), unique = True)
	firstName = db.Column(db.String(100), nullable = False)
	lastName = db.Column(db.String(100), nullable = False)
	username = db.Column(db.String(100), unique=True, nullable = False)
	password = db.Column(db.String(255), nullable = False)
	address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)

	address = db.relationship('Address', backref='account')

	def __init__(self, public_id, firstName, lastName, username, password):
		self.public_id = public_id
		self.firstName = firstName
		self.lastName = lastName
		self.username = username
		self.password = password

	def add_db_account(self):
		db.session.add(self)
		db.session.commit()

	def update_db_account(self):
		db.session.commit()

	def delete_db_account(self):
		db.session.delete(self)
		db.session.commit()

@jwt.user_identity_loader
def user_identity_lookup(valid_username):
    return valid_username.public_id