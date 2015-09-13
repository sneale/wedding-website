import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from wedding import db

class Guest(db.Model):
	"""Guest Model"""
	__tablename__ = 'guest'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(70), unique=True)
	email = db.Column(db.String(120), unique=True)
	plus_one = db.Column(String(70))
	date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
	count = db.Column(db.Integer)
	comments = db.Column(db.Text(length=None))
	attending = db.Column(db.Text)

	def __init__(self, name, email=None, plus_one=None, date=None, count=1, attending="Yes", comments=None):
		self.name = name
		self.email = email
		self.plus_one = plus_one
		self.attending = attending
		self.regdate = datetime.datetime.now()

		if self.attending:
			self.count = 1
			if self.plus_one and self.plus_one != "":
				self.count = 2
		else:
			self.count = 0

		self.comments = comments

	def __repr__(self):
		return '<User %r>' % (self.name)

db.create_all()