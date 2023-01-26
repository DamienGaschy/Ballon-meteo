#bibliothèque

import psycopg2
import psycopg2.extras
from flask import Flask, request
from flask_restx import Resource, Api
import api

#_________________________________________________________________________________

#application description

app = Flask(__name__)
# api = Api(app)
api = Api(app=app, version="0.1", doc="/api", title="Api", description="Cette API est utilisée par une station météo", default="api", default_label='API Météo', validate=True)

todos = {}
#_________________________________________________________________________________

#connexion base de donnée postgre

# conn = psycopg2.connect(host="localhost", dbname="Balloon_Boy", user="postgres", password="2003", port="5432")
# cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
host="localhost"
dbname="Balloon_Boy"
user="postgres"
password="2003"
port="5432"
cursor_factory = psycopg2.extras.RealDictCursor

#_________________________________________________________________________________

#prise donnée température

@app.route('/temp', methods=['POST'])
def temp():
    conn = psycopg2.connect(host=host,dbname=dbname,user=user,password=password,port=port)
    cursor = conn.cursor(cursor_factory=cursor_factory)
    posttemp = "INSERT INTO meteo (temperature , humidite) VALUES (%s,%s)"
    value = ('temperature' , 'humidite')
    cursor.execute(posttemp, value)
    conn.commit()
    conn.close()
    return "Data inserted successfully!"

#_________________________________________________________________________________

#prise donnée humidité

# @app.route('/humi', methods=['POST'])
# def temp():
#     conn = psycopg2.connect(host=host,dbname=dbname,user=user,password=password,port=port)
#     cursor = conn.cursor(cursor_factory=cursor_factory)
#     posttemp = "INSERT INTO meteo (temperature , humidite) VALUES (%s,%s)"
#     value = ('', '')
#     cursor.execute(posttemp, value)
#     conn.commit()
#     conn.close()

#_________________________________________________________________________________

#derniere donnée

@app.route('/last', methods=['GET'])
def last():
    conn = psycopg2.connect(host=host,dbname=dbname,user=user,password=password,port=port)
    cursor = conn.cursor(cursor_factory=cursor_factory)
    cursor.execute("SELECT * FROM meteo ORDER BY id DESC LIMIT 1")
    # conn.commit()
    result=cursor.fetchall()
    conn.close()
    return result

#_________________________________________________________________________________

#toutes les données

@app.route('/all', methods=['GET'])
def all():
    conn = psycopg2.connect(host=host,dbname=dbname,user=user,password=password,port=port)
    cursor = conn.cursor(cursor_factory=cursor_factory)
    cursor.execute("SELECT * FROM meteo ")
    # conn.commit()
    result=cursor.fetchall()
    conn.close()
    return result

#_________________________________________________________________________________

if __name__ == '__main__':
    app.run(debug=True)