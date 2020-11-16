from flask import Flask, render_template
from jogo import Jogo
import leitor

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = leitor.le_jogos()
    return render_template('lista.html', titulo="Jogos", jogos=lista)

app.run()