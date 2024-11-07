from flask import Flask, render_template, request, redirect, url_for
from models import JogoMemoria

app = Flask(__name__)
jogo = JogoMemoria()  

@app.route('/')
def index():
 
    global jogo  
    jogo = JogoMemoria() 
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        indice = int(request.form['indice'])
        resultado = jogo.selecionar_carta(indice)

        if resultado is False:  
            return render_template('game.html', cartas=jogo.cartas, vira_depois=True)

        if jogo.jogo_completo():
            return redirect(url_for('vitoria'))

    return render_template('game.html', cartas=jogo.cartas, vira_depois=False)

@app.route('/desvirar')
def desvirar():
    jogo.desvirar_cartas() 
    return redirect(url_for('game'))

@app.route('/vitoria')
def vitoria():
    return '''
    <h1>Você encontrou todos os pares!</h1>
    <a href="{0}">
        <button>Reiniciar Jogo</button>
    </a>
    '''.format(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
