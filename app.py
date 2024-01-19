from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
from config import DATABASE_URI


app=Flask(__name__)
app.config['SECRET_KEY']='secret-key'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URI
db=SQLAlchemy(app)

# with app.app_context():
#     # Create the tables in the database
#     db.create_all()



# class Task(db.Model):
#     __tablename__ = 'applications'
#     id=db.Column(db.Integer,primary_key=True)
#     title=db.Column(db.String(100),primary_key=True)
#     dt=db.Column(db.Date)
#     def __init__(self,title):
#         self.title=title
#         sql_datetime = datetime.now().strftime('%Y-%m-%d')
#         self.dt=sql_datetime

#     def __repr__(self):
#         return f'{self.title} created on {self.date}'
    
# with app.app_context():
#     new_task = Task(title='flask')
#     db.session.add(new_task)
#     db.session.commit()

from routes import *

if __name__=='__main__':
    app.run(debug=True)
