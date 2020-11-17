from flask import Flask, render_template, request, redirect, session, flash, url_for
from jogo import Jogo
import arquivo

app = Flask(__name__)
app.secret_key = 'andrey'

@app.route('/')
def lista():
    lista = arquivo.le_jogos()
    return render_template('lista.html', titulo="Jogos", jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods=["POST"])
def criar():
    jogo = Jogo(request.form['nome'], request.form['categoria'], request.form['console'])
    arquivo.escreve(jogo)
    return redirect(url_for('lista'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/auth', methods=["POST"])
def auth():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash('{} logou com sucesso!'.format(request.form['usuario']))
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Não logado, Tente novamente!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('lista'))

app.run(debug=True)