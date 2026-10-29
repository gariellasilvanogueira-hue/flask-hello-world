
import os
from datetime import datetime
from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

anotacoes = []

@app.route('/')
def inicio():
    print('Acesso à página inicial', flush=True)
    mensagem = os.getenv('MENSAGEM', 'Olá, FASF!')
    return f'<h1>{mensagem}</h1><p>Aula de PaaS</p>'

@app.route('/sobre')
def sobre():
    return 'Computação em Nuvem - FASF - Aula do Nilton'

@app.route('/anotacoes', methods=['GET', 'POST'])
def pagina_anotacoes():
    if request.method == 'POST':
        assunto = request.form.get('assunto', '').strip()
        anotacao = request.form.get('anotacao', '').strip()

        if assunto and anotacao:
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
            anotacoes.append([data, assunto, anotacao])

        return redirect(url_for('pagina_anotacoes'))

    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Tabela de Anotações</title>
    </head>
    <body>
        <h1>Tabela de Anotações</h1>

        <form method="POST">
            <label>Assunto:</label><br>
            <input type="text" name="assunto" required><br><br>

            <label>Anotação:</label><br>
            <textarea name="anotacao" required></textarea><br><br>

            <button type="submit">Adicionar anotação</button>
        </form>

        <h2>Anotações registradas</h2>

        <table border="1" cellpadding="8">
            <tr>
                <th>Data</th>
                <th>Assunto</th>
                <th>Anotação</th>
            </tr>

            {% for item in anotacoes %}
            <tr>
                {% for campo in item %}
                <td>{{ campo }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>

        <p><a href="/">Página inicial</a></p>
        <p><a href="/sobre">Sobre</a></p>
    </body>
    </html>
    '''

    return render_template_string(html, anotacoes=anotacoes)

if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=porta)
