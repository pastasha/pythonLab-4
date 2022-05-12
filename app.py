import requests
from flask import Flask, render_template,request
import psycopg2

app = Flask(__name__)
conn=psycopg2.connect(database="service_db",
                      user="postgres",
                      password="12345",
                      host="localhost",
                      port="5432")
cursor=conn.cursor()

@app.route('/login/',methods=['get'])
def index():
    return render_template('login.html')

@app.route('/login/',methods=['post'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    if username =="" or password=="":
        return render_template('login.html')

    
    cursor.execute("select * from service.users where login ='{}' and password = '{}'".format(str(username),str(password)))
    records=list(cursor.fetchall())

    if len(records)==0:
        return render_template('login.html')

    return render_template('account.html',b_data=records[0][1:])
