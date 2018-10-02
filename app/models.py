from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  def __repr__(self):
    return '<User {}>'.format(self.username)

class Ticket(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  buyer_email = db.Column(db.String(128), index=True, unique=True)
  buyer_tel = db.Column(db.String(16))
  quanlity = db.Column(db.Integer)
  bought_at = db.Column(db.DateTime())
  amount = db.Column(db.Integer)

  def __repr__(self):
    return '<Ticket {}>'.format(self.id)
