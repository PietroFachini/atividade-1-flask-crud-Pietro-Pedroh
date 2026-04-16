class Peca:

    contador = 1

    def __init__(self, nome, descricao, veiculo, preco):
        self.nome = nome
        self.descricao = descricao
        self.veiculo = veiculo
        self.preco = preco
        Peca.contador += 1
        self.id = Peca.contador

    def to_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "Veiculo": self.veiculo,
            "preco": self.preco,
            "id": self.id 
        }
    
