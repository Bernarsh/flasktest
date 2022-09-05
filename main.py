from flask import Flask, escape, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<html> <head> <title>Minha página </title> </head> <body> <b> Hello, from Flask! </b> </body> </html>'
  
@app.route('/ola/<int:idade>')
def thyago(idade):
  return '<b>A idade do usuário é <b>' + str(idade)

@app.route('/olatemplate/')       
@app.route('/olatemplate/ <nome>')         
def ola(nome = 'Fulano'):
  
  return render_template('ola.html', variavel = nome)
  
@app.route('/formulario')
def form():
  return render_template('formulario.html')
  
@app.post('/boasvindas')
def bemvindo():
  nome = request.form['nome']
  return 'Ainn, ' + nome + ', ' + 'fuma um cigarrinho pra mim, fuma'
  
app.run(host='0.0.0.0', port=81)