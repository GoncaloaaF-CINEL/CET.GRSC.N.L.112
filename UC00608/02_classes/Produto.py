
class Produto:
    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = float(preco)


    # dunder method
    def __str__(self):
        return f"nome: {self.nome}\tpreço: {self.preco:.2f}€"

    def __repr__(self):
        return f"nome: {self.nome}\tpreço: {self.preco:.2f}€"

    def __gt__(self, produto):
        return self.preco > produto.preco



# p = Produto("Picanha", 100)
# p2 = Produto("Picanha", 100)

# print(p)
# print(p == p2)