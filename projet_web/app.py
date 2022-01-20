import sqlite3
from flask import Flask, render_template, request
import data
import psycopg2
import pymysql
import re



cursor = None
app = Flask(__name__)




def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/don')
def don():
    return render_template('don.html')


@app.route('/don', methods=['GET', 'POST'])
def recup_info():
    if request.method == 'GET':
        # send the form
        return render_template('don.html')

    # handle the POST request
    if request.method == 'POST':
        titre = request.form.get('titre')
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        mail = request.form.get('email')
        montant = request.form.get('don')
        data.ecrire_dons(titre, nom, prenom, mail, montant)
        return render_template('merci.html')


@app.route('/merci')
def merci():
    return render_template('merci.html')


@app.route('/info_don')
def info_don():
    host='localhost'
    user = 'root'
    password = 'root'
    port = 8081
    db = 'flask_don'
    con = pymysql.connect(host=host,user=user,password=password,db=db, port=port, use_unicode=True, charset='utf8')
    cur = con.cursor()
    cur.execute("SELECT * FROM dons")
    data = cur.fetchall()
    cur.execute("SELECT sum(montant) as total_don FROM dons")
    total = cur.fetchall()
    return render_template('info_don.html', data=data, total=total)


