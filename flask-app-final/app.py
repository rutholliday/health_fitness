
import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Hoosier36#^@localhost:3306/health_wellness_db'
 
db = SQLAlchemy(app)
 
 
class Spas(db.Model):
    __tablename__ = "spas"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Spa: {}>".format(self.name)

class Influencers(db.Model):
    __tablename__ = "influencers"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Influencer: {}>".format(self.name)

class OrganicNYT(db.Model):
    __tablename__ = "organic"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Organic: {}>".format(self.name)

class VeganNYT(db.Model):
    __tablename__ = "vegan"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Vegan: {}>".format(self.name)

class VegetarianNYT(db.Model):
    __tablename__ = "vegetarian"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Vegetarian: {}>".format(self.name)

class FitnessNYT(db.Model):
    __tablename__ = "fitness"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Fitness: {}>".format(self.name)

class ExerciseNYT(db.Model):
    __tablename__ = "exercise"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Exercise: {}>".format(self.name)

class AnxietyNYT(db.Model):
    __tablename__ = "anxiety"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Anxiety: {}>".format(self.name)

class DepressionNYT(db.Model):
    __tablename__ = "depression"
 
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
 
    def __repr__(self):
        return "<Depression: {}>".format(self.name)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

Spas = Base.classes.spa_website_launches
Influencers = Base.classes.influencer_website_launch_dates
OrganicNYT = Base.classes.organic_frequency_nyt
VeganNYT = Base.classes.vegan_frequency_nyt
VegetarianNYT = Base.classes.vegetarian_frequency_nyt
FitnessNYT = Base.classes.fitness_frequency_nyt
ExerciseNYT = Base.classes.exercise_frequency_nyt
DepressionNYT = Base.classes.depression_frequency_nyt
AnxietyNYT = Base.classes.anxiety_frequency_nyt


spa_data = db.session.query(Spas.year, Spas.count)
influencer_data = db.session.query(Influencers.year, Influencers.count)
organic_nyt_data = db.session.query(OrganicNYT.year, OrganicNYT.organic_frequency)
vegan_nyt_data = db.session.query(VeganNYT.year, VeganNYT.fitness_frequency)
vegetarian_nyt_data = db.session.query(VegetarianNYT.year, VegetarianNYT.fitness_frequency)
fitness_nyt_data = db.session.query(FitnessNYT.year, FitnessNYT.fitness_frequency)
exercise_nyt_data = db.session.query(ExerciseNYT.year, ExerciseNYT.exercise_frequency)
depression_nyt_data = db.session.query(DepressionNYT.year, DepressionNYT.depression_frequency)
anxiety_nyt_data = db.session.query(AnxietyNYT.year, AnxietyNYT.anxiety_frequency)

spa_count = list(map(list, zip(*spa_data)))
influencer_count = list(map(list, zip(*influencer_data)))
organic_nyt_count = list(map(list, zip(*organic_nyt_data)))
vegan_nyt_count = list(map(list, zip(*vegan_nyt_data)))
vegetarian_nyt_count = list(map(list, zip(*vegetarian_nyt_data)))
fitness_nyt_count = list(map(list, zip(*fitness_nyt_data)))
exercise_nyt_count = list(map(list, zip(*exercise_nyt_data)))
depression_nyt_count = list(map(list, zip(*depression_nyt_data)))
anxiety_nyt_count = list(map(list, zip(*anxiety_nyt_data)))

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/spa")
def spa():
    data = [{
        "x": spa_count[0],
        "y": spa_count[1]
        }]

    return jsonify(data)

@app.route("/influencer")
def influencer():
    data = [{
        "x": influencer_count[0],
        "y": influencer_count[1]
        }]

    return jsonify(data)

@app.route("/vegan")
def vegan():
    data = [{
        "x": vegan_nyt_count[0],
        "y": vegan_nyt_count[1]
        }]

    return jsonify(data)

@app.route("/vegetarian")
def vegetarian():
    data = [{
        "x": vegetarian_nyt_count[0],
        "y": vegetarian_nyt_count[1]
        }]

    return jsonify(data)

@app.route("/fitness")
def fitness():
    data = [{
        "x": fitness_nyt_count[0],
        "y": fitness_nyt_count[1]
        }]

    return jsonify(data)

@app.route("/exercise")
def exercise():
    data = [{
        "x": exercise_nyt_count[0],
        "y": exercise_nyt_count[1]
        }]

    return jsonify(data)

@app.route("/depression")
def depression():
    data = [{
        "x": depression_nyt_count[0],
        "y": depression_nyt_count[1]
        }]

    return jsonify(data)

@app.route("/anxiety")
def anxiety():
    data = [{
        "x": anxiety_nyt_count[0],
        "y": anxiety_nyt_count[1]
        }]

    return jsonify(data)

@app.route("/organic_nyt")
def organic_nyt():

    df = pd.DataFrame(data={
        'year': organic_nyt_count[0],
        'count': organic_nyt_count[1]
        })
    
    df = df.astype(float)

    chart_data = df.to_dict(orient='records')

    data = jsonify(chart_data)

    return data


if __name__ == "__main__":
    app.run(debug=True)