#This project is a follow along from freeCodeCamp
#I do not take credit for this code and it is for educational purposes only
#https://www.freecodecamp.org/news/build-a-simple-json-api-in-python/




from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flash(__name__) #Create a flask application here, like INIT

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////artists.db'
db = SQLAlchemy(app)

#Here you define a class for table Artist
#This is the format model for our JSON data

class Artist(db.model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string)
    birth_year = db.Column(db.Integer)
    genre = db.Column(db.String)

#Create the table
db.create_all()
