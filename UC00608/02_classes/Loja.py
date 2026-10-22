from Produto import Produto





class Loja:

    def __init__(self, lista_produtos:list[Produto] = []):
        self.__lista_produtos = lista_produtos # prop privada | Lista de class


    def lista_produtos(self):

        if len(self.__lista_produtos) == 0:
            print("Lista vazia")
            return

        for produto in self.__lista_produtos:
            print(produto)

    def __metodo_privado(self): # metodo privada
        pass

    # crie um metodo para add produtos
    def adiciona_produto(self, *produto:Produto):  # usar uma class dentro de outra
        self.__lista_produtos.extend(produto)


    # crie um metodo para add produtos, indicando os dados do produto

    # crie um metodo que verifique se um produto existe
