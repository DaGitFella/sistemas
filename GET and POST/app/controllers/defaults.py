from app import app
from flask import render_template, request

@app.route('/')
def index():
    return 'hello everyone!'

@app.route('/dados')
def dados():  
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST'])
def receba():
    nome = request.form['nome']
    email = request.form['email']
    estado = request.form['estado']
    return render_template('mostrar.html', nome=nome, email=email, estado=estado)
