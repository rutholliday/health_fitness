#import dependencies
import pandas as pd
import numpy as np

# SQL Alchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# PyMySQL
import pymysql
pymysql.install_as_MySQLdb()
\
#flask
from flask import Flask, jsonify, render_template

#just have to change this to your password for local access to your sqlsql database
sql_password = 'CassiusClay2!'
db_name = 'Health_Trend_Project_db'

#connecting to my sql database
rds_connection_string = "root:"+sql_password+"@127.0.0.1/"+db_name
engine = create_engine(f'mysql://{rds_connection_string}')
conn = engine.connect()
session = Session(bind=engine)


#Starting Flask App
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/National_Health_Exp")
def National_Health_Expenses():
    #Queries the national health expenditures data
    Nat_Health_Exp = pd.read_sql("SELECT * FROM national_health_expenditures_data", conn)

    #making the pandas dataframe a json file
    Nat_health_Exp_jsonfile = Nat_Health_Exp.to_json(orient='records')

    #or just return "Nat_health_Exp_jsonfile" because it is technically already in json file
    return jsonify(Nat_health_Exp_jsonfile)

@app.route("/US_CDI_info")
def National_Health_Expenses():
    #Queries the US CDI database
    US_CDI_tb = pd.read_sql("select US_CDI.YearStart, US_CDI.LocationAbbr, US_CDI.Topic, US_CDI.Question, US_CDI.DataValue\
                        from US_Chronic_Disease_Indicators_Data  US_CDI where US_CDI.LocationAbbr = 'US'", conn)

    #making the pandas dataframe a json file
    US_CDI_info_jsonfile = US_CDI_tb.to_json(orient='records')

    #or just return "US_CDI_info_jsonfile" because it is technically already in json file
    return jsonify(US_CDI_info_jsonfile)


if __name__ == "__main__":
    app.run(debug=True)
