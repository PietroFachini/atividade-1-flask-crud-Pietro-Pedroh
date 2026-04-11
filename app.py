from flask import Flask, jsonify, request #redirect
from peca import Peca
from flask import Request

app = Flask(__name__)

pecas = []

peca1 = Peca("correia", "correia top", "Fiat Mobi", 30)

pecas.append(peca1)

@app.route("/", methods=["GET"])
def pagina_inicial():
    return jsonify([peca.to_dict() for peca in pecas])
    #Depois precisa utilizar o render quando for usar o html

@app.route("/", methods=["POST"])
def publicar():
    dados = request.get_json()
    #nome = Request.form["nome"]
    #descricao = Request.form["descricao"]
    #veiculo = Request.form["veiculo"]
    #preco = float(Request.form["preco"])
    #nova_peca = Peca(nome, descricao, veiculo, preco)
    nova_peca = Peca(dados["nome"], dados["descricao"], dados["veiculo"], dados["preco"])
    pecas.append(nova_peca)
    #return redirect("/")
    return jsonify(nova_peca.to_dict()), 201
    #Já deixei codigo pronto pra quando o HTML estiver pronto
    #TUDO TESTADO BONITINHO NO POSTMAN, 201 É SÓ PRA QUEM PODE PAPAI



if __name__ == "__main__":
    app.run(debug=True)