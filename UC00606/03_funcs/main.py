"""
var
op com var
condições
    if elif else
    match

range

loops
    for
    while

funcs

"""


def ola_mundo():
    print("|-------------|")
    print("|  ola mundo  |")
    print("|-------------|")


ola_mundo()
ola_mundo()
ola_mundo()


def ola_mundo2(nome:str):
    # pass # <- criar um bloco vazio (para não dar erro)
    print(f"ola mundo, {nome}")

ola_mundo2("Joao")
ola_mundo2("Maria")
ola_mundo2(1234)

def ola_mundo3(nome:str, idade:int):
    # pass # <- criar um bloco vazio (para não dar erro)
    print(f"ola mundo, {nome}, tens {idade} anos")

ola_mundo3("Joao", 12)
ola_mundo3("Maria", 14)
ola_mundo3("Maria", "Dez")

def ola_mundo4(nome:str, idade:int = 15):
    # pass # <- criar um bloco vazio (para não dar erro)
    print(f"ola mundo, {nome}, tens {idade} anos")


ola_mundo4("Joao", 114)
ola_mundo4("Joao" )


def ola_mundo4(nome:str, idade:int, ano:int):
    # pass # <- criar um bloco vazio (para não dar erro)
    print(f"ola mundo, {nome}, tens {idade} anos no ano {ano}")


ola_mundo4("Joao", 11, 2026)

ola_mundo4(nome="Joao", idade=11, ano=2024)

ola_mundo4(idade=11,ano=2024, nome="Joao" )

ola_mundo4("Maria", idade=11, ano=2024)


def e_par(num:int):
    if num % 2 == 0:
        return True
    else:
        return False

def e_par2(num:int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False
    
res = e_par(5)
print(res)

res = e_par(6)
print(res)
