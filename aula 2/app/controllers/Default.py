from app import app
from flask import render_template

@app.route('/')
def index():
    return 'hello world!'

@app.route('/compras')
def compras():
    return render_template('compras.html', nome_da_minha_mae='Letícia')

@app.route('/mercados')
def mercado():
    return render_template('mercados.html')