from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def ola_mundo():
    titulo = "Povo da minha família"
    usuarios = [
        {"nome": "Judson", "membro_ativo": True},
        {"nome": "Karine", "membro_ativo": True},
        {"nome": "Matheus", "membro_ativo": False},
        {"nome": "Tayná", "membro_ativo": False}        
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)


@app.route('/sobre')
def pagina_sobre():
    return f"""<p>
    <b> Este site está sendo construído como forma de aprendizado. </b>
    </p>
    <a href= "https://www.google.com.br"> Site do Google </a>  
    </p>
    <a></a>   
    <a href= {url_for('ola_mundo')}> Página Inicial </a>"""

app.run(debug=True)