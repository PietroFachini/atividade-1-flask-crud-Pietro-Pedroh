from flask import Flask, jsonify, request, redirect, render_template
from peca import Peca
from flask import Request

app = Flask(__name__)

pecas = []

peca1 = Peca("correia", "correia top", "Fiat Mobi", 30)

pecas.append(peca1)

@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html", pecas = pecas)
    #Depois precisa utilizar o render quando for usar o html

@app.route("/pecas", methods=["GET"])
def listar_pecas():
    return jsonify([peca.to_dict() for peca in pecas])

@app.route("/pecas", methods=["POST"])
def publicar():
    #dados = request.get_json()
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    veiculo = request.form["veiculo"]
    preco = float(request.form["preco"])
    nova_peca = Peca(nome, descricao, veiculo, preco)
    #nova_peca = Peca(dados["nome"], dados["descricao"], dados["veiculo"], dados["preco"])
    pecas.append(nova_peca)
    return redirect("/")
    #return jsonify(nova_peca.to_dict()), 201
    #Já deixei codigo pronto pra quando o HTML estiver pronto
    #TUDO TESTADO BONITINHO NO POSTMAN, 201 É SÓ PRA QUEM PODE PAPAI

@app.route("/remover/<int:id>")
def remover_pecas(id):
    global pecas
    pecas = [peca for peca in pecas if peca.id != id]
    return redirect("/")


@app.route("/editar/<int:id>")
def editar_pecas(id):
    peca = next((peca for peca in pecas if peca.id == id), None)
    if peca:
        return render_template("editar.html", peca=peca)
    return redirect("/")


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_pecas(id):
    peca = next((peca for peca in pecas if peca.id == id), None)
    if peca:
        peca.nome = request.form["nome"]
        peca.descricao = (request.form["descricao"])
        peca.veiculo = (request.form["veiculo"])
        peca.preco = float(request.form["preco"])
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)