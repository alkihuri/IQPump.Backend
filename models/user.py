
from db import db
from datetime import datetime   

class User(db.Model):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.active = True
        self.created_at = datetime.datetime.now()
        