#bibliothèque

import mysql.connector
from flask import Flask, request
from flask_restx import Resource, Api
from db_connection import connect_to_db

#_________________________________________________________________________________

#application description

app = Flask(name)

api = Api(app)
api = Api(app=app, version="0.1", doc="/api", title="Api", description="Cette API est utilisée par une station météo", default="api", default_label='API Météo', validate=True)

#_________________________________________________________________________________

#connexion base de donnée postgre

conn = mysql.connector.connect(host="localhost", dbname="Balloon_Boy", user="postgres", password="2003", port="5432")
cursor = conn.cursor(cursor_factory = mysql.connector.cursor.MySQLCursorDict)
host="localhost"
dbname="Balloon_Boy"
user="postgres"
password="2003"
port="5432"
cursor_factory = mysql.connector.cursor.MySQLCursorDict

#_________________________________________________________________________________

#prise donnée température

@app.route('/temp', methods=['POST'])
def temp():
conn = mysql.connector.connect(host=host,dbname=dbname,user=user,password=password,port=port)
cursor = conn.cursor(cursor_factory=cursor_factory)
posttemp = "INSERT INTO meteo (temperature ,humidite) VALUES (%s,%s)"
value = ('temperature' , 'humidite')
cursor.execute(posttemp, value)
conn.commit()
cursor.close()
conn.close()
return "Data inserted successfully!"

#_________________________________________________________________________________

#derniere donnée

@app.route('/last', methods=['GET'])
def last():
conn = mysql.connect(host=host,dbname=dbname,user=user,password=password,port=port)
cursor = conn.cursor(cursor_factory=cursor_factory)
cursor.execute("SELECT * FROM meteo ORDER BY id DESC LIMIT 1")
# conn.commit()
result=cursor.fetchall()
cursor.close()
conn.close()
return result

#_________________________________________________________________________________

#toutes les données

@app.route('/all', methods=['GET'])
def all():
conn = mysql.connect(host=host,dbname=dbname,user=user,password=password,port=port)
cursor = conn.cursor(cursor_factory=cursor_factory)
cursor.execute("SELECT * FROM meteo ")
# conn.commit()
result=cursor.fetchall()
cursor.close()
conn.close()
return result

#_________________________________________________________________________________

if name == 'main':
conn = connect_to_db()
app.run(host='127.0.0.1',debug=True)


