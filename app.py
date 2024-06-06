import os
import csv
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Preparação para o ambiente Flask em Desenvolvento
os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

# Rotas do Projeto
@app.route('/')
def index():
    '''Listar o glossário'''

    # Criação de lista vazia
    glossario_de_termos = []

    # Abrir o arquivo e colocá-lo dentro da lista

    with open('bd_glossario.csv',
            newline='',
            encoding='utf-8') as arquivo:
     leitor = csv.reader(arquivo, delimiter=';')

    for linha  in leitor:
     glossario_de_termos.append(linha)

     return render_template('index.html'),
     glossario_de_termos=glossario_de_termos


@app.route('/novo-termo')
def novo_termo():
    return render_template(('adicionar_termo.html'))


@app.route('/criar_termo', methods=['POST',])
def criar_termo():

    termo = request.form['termo']
    definicão = request.form['definicão']


    with open('bd_glossario.csv',
              'a',
              newline='',
              encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow([termo, definicão])

        return redirect(url_for('index'))



@app.route('/excluir_termo/<int:termo_id>', methods=['POST',])
def excluir_termo(termo_id):

      with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
          leitor = csv.reader(arquivo)
          linhas =  list(list.leitor)

      for i, linha in enumerate(linhas):
          if i == termo_id:
              del linhas
              break

      with open('bd_glossario.csv',
              'a',
              newline='',
              encoding='utf-8') as arquivo:
       escritor = csv.writer(arquivo)
       escritor.writerows(linhas)

       return redirect(url_for('index.html'))


if __name__ == '__main__':
    app.run()