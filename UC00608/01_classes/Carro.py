class Carro:

    def __init__(self, marca:str, modelo:str, year:int): # Construtor
        self.marca = marca
        self.modelo = modelo
        self.ano = year

    #                    typ hint -> return
    def get_info(self) -> str:
        return f"{self.marca} {self.modelo} de {self.ano}"

    def show_info(self):
        print( f"{self.marca} {self.modelo} de {self.ano}")

    # crie um metodo para alterar o ano do carro

    def mudar_ano(self, novo_ano):
        # garanta que o ano não é menor que 1886
        # e não é maior que 2027

        # if 1886 <= novo_ano < 2027:
        #    self.ano = novo_ano

        #if 1886 <= novo_ano and novo_ano < 2027:
        #    self.ano = novo_ano

        # if not (1886 >= novo_ano or novo_ano > 2027):
        #   self.ano = novo_ano

        self.ano = novo_ano if  1886 <= novo_ano < 2027 else self.ano

    # pass #  pass <-- Cria um bloco vazio


