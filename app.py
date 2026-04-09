from flask import Flask, jsonify
from peca import Peca
from flask import Request

app = Flask(__name__)

pecas = []

peca1 = Peca("correia", "correia top", "Fiat Mobi", 30)

pecas.append(peca1)

@app.route("/", methods=["GET"])
def pagina_inicial():
    return jsonify([peca.to_dict() for peca in pecas])



if __name__ == "__main__":
    app.run(debug=True)