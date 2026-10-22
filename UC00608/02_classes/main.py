from Loja import Loja
from Produto import Produto


"""
lista_produtos:list[Produto] = []

p1 = Produto("Picanha", 20)
lista_produtos.append(p1)

lista_produtos.append( Produto("Maminha", 25))



print("---- Criar novo porduto -----")

nome = input("Nome: ")
preco = float(input("Preço: "))

novo_produto = Produto(nome, preco)
lista_produtos.append(novo_produto)


print("---------")
for idx, produto in enumerate(lista_produtos, start=1):
    print(f"produto {idx}: {produto}")

"""

loja = Loja([ Produto("Maminha", 25),  Produto("Picanha", 25)])
loja2 = Loja()

loja.lista_produtos()
loja2.lista_produtos()

loja.adiciona_produto(
    Produto("Lombo", 50),
    Produto("Alcatra", 15)
)

loja.lista_produtos()

"""
def teste (*args):
    for elm in args:
        print(elm * 3)

teste(12,41,41)

"""