from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SECRET_KEY']='secret-key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

db=SQLAlchemy(app)

with app.app_context():
    # Create the tables in the database
    db.create_all()



from routes import *

if __name__=='__main__':
    app.run(debug=True)


# class Task(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     title=db.Column(db.String(100),nullable=False)
#     date=db.Column(db.Date,nullable=False)

#     def __init__(self, title, date):
#         self.title = title
#         self.date = date

#     def __repr__(self):
#         return f'{self.title} created on {self.date}'
# with app.app_context():
#     db.create_all()

#     db.session.add(Task('admin', date=datetime.utcnow()))
#     db.session.add(Task('guest', date=datetime.utcnow()))
#     db.session.commit()

#     users = Task.query.all()
#     print(users)