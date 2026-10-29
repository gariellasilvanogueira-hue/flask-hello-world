import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    print ('Acesso a Pagina inicial', flush=True)
    mensagem = os.getenv('MENSAGEM', 'Ola, Fasf!')
    return f'<h1>{mensagem}</h1><p>Aula de PaaS<p>'

@app.route('/sobre')
def sobre():
    return 'Computacao em Nuvem -FASF AULA DO NILTON'
    
