from app import db
from datetime import datetime
import random



class Task(db.Model):
    __tablename__ = 'applications'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    dt=db.Column(db.Date)
    def __init__(self,title):
        self.id=random.randint(1, 100000)
        self.title=title
        sql_datetime = datetime.now().strftime('%Y-%m-%d')
        self.dt=sql_datetime
    def __repr__(self):
        return f'{self.title} created on {self.date}'