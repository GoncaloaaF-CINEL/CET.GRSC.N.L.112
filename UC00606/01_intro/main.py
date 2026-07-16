# cmt

"""
Cmt
multi
linha
"""


"""
var
    tipos de dados
    op com var

int
float
string
bool

"""


idade = 10
nome = "Ana"

print(idade, nome)

#                       conveter a idade para int
#                                   |
#                                   v
print("a "+ nome + " tem " + str(idade) + " anos")

print(f"a {nome} tem {idade} anos")

idade = 20
print(f"a {nome} tem {idade} anos")

idade = "Dez" # <-- Evitar mudar dinamicamente o tipo da var
print(f"a {nome} tem {idade} anos")


# type hint
media: float = 3.5
print(type(media))
print(media)
media = 10
print(type(media))
print(media)

media = "Dez"
print(media)
print(type(media))


"""

tipos base

int
float
str
bool
"""


n1 = 10
n2 = 30

print("---------------")
soma = n1 + n2
print(soma)
print(type(soma))


sub = n1 - n2
print(sub)
print(type(sub))



multip = n1 * n2
print(multip)
print(type(multip))



div = n1 / n2 # -> devolve sp float
print(div)
print(type(div))

n1 = 10
n2 = 5
div = n1 / n2  # -> devolve sp float
print(div)
print(type(div))



n1 = 30
n2 = 4
div_i = n1 // n2  # -> // -> div int
print(div_i)
print(type(div_i))

n1 = 30
n2 = 4
mod = n1 % n2  # -> // -> div int
print(mod)
print(type(mod))


print("---------------")

print("Ola " + "Mundo")
print("Ola " * 10)

print("-_-" * 5)



n1 = 10.0
n2 = 30.

print("---------------")
soma = n1 + n2
print(soma)
print(type(soma))


sub = n1 - n2
print(sub)
print(type(sub))


multip = n1 * n2
print(multip)
print(type(multip))



div = n1 / n2 # -> devolve sp float
print(div)
print(type(div))

n1 = 10.0
n2 = 5.
div = n1 / n2  # -> devolve sp float
print(div)
print(type(div))



n1 = 30.0
n2 = 4.
div_i = n1 // n2  # -> // -> div int
print(div_i)
print(type(div_i))

n1 = 30.0
n2 = 4.
mod = n1 % n2  # -> // -> div int
print(mod)
print(type(mod))

print("-" * 10)

"""

var
    tipos de dados
    op com var

saida de dados 
    print

Entrada de dados
"""

nome = input("Digite seu nome: ") # input recebe sempre uma str


#          converter uma str para int
idade = int(input("Digite sua idade: "))

ano_nasc = 2026-idade

print(f"ola {nome} nasceste em {ano_nasc}")

"""
var: x
novo_tipo(var)  -> estão a converter a var do tipo x para o novo_tipo
"""

base = 2
exp = 10
# 2^10

print(2 ** 10) # * -> vezes | ** -> elevado a 
print(pow(base, exp))