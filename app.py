import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "pudim"


app = Flask(__name__)
app.config.from_object(__name__)

def db_connect():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_request():
    g.db = db_connect()

@app.teardown_request
def pos_request(exception):
    g.db.close()

@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto from entradas ORDER BY id DESC"
    cur = g.db.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo':titulo, 'texto':texto})
    return str(entradas)
    
@app.route('/pudim')
def pudim():
    return "<h1 style='color: red;'>Eu gosto de PUDIM!</h1>"