from flask import Flask, render_template, request, redirect, url_for
from models import JogoMemoria, CartaVirada, CartaNormal

# Inicializando o Flask e criando uma instância do jogo
app = Flask(__name__)
jogo = JogoMemoria()  

# Rota inicial 
@app.route('/')
def index():
    global jogo
    jogo = JogoMemoria()  
    return render_template('index.html') 

# Rota onde o jogo é jogado
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

# Rota para desvirar cartas selecionadas
@app.route('/desvirar')
def desvirar():
    jogo.desvirar_cartas() 
    return redirect(url_for('game')) 

@app.route('/vitoria')
def vitoria():
    return render_template('./winner.html')
   

# Inicia o servidor Flask 
if __name__ == '__main__':
    app.run(debug=True)
