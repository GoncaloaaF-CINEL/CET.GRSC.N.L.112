"""
cmt
    1 linha
    multi linha

var
tipos de dados
op com var
condições (if, match)
loop (for, while)
listas (arrays)
set
tuplos
dict
funcs


"""
from unittest import case


# Crie uma função que receba um num (1 as 12) e diga o mês, se o mes for invalido deve dar essa indicação


def mes(num:int):
    if num == 1:
        return "Jan"
    elif num == 2:
        return "Feb"
    elif num == 3:
        return "Mar"
    elif num == 4:
        return "Apr"
    elif num == 5:
        return "May"
    elif num == 6:
        return "Jun"
    elif num == 7:
        return "Jul"
    elif num == 8:
        return "Aug"
    elif num == 9:
        return "Sep"
    elif num == 10:
        return "Oct"
    elif num == 11:
        return "Nov"
    elif num == 12:
        return "Dec"
    else:
        return "Mes Invalido"


def mes_v2(num:int):
    match num:
        case 1:
            return "Jan"
        case 2:
            return "Feb"
        case 3:
            return "Mar"
        case 4:
            return "Apr"
        case 5:
            return "May"
        case 6:
            return "Jun"
        case 7:
            return "Jul"
        case 8:
            return "Aug"
        case 9:
            return "Sep"
        case 10:
            return "Oct"
        case 11:
            return "Nov"
        case 12:
            return "Dec"
        case _:
            return "Mes Invalido"


def mes_v3(num:int):
    meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    if num < 1 or num > len(meses):
        return "mes Invalido"

    return meses[num-1]


def mes_v4(num:int):
    meses = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
             7:"Jul",8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}

    return meses[num] # --> se a key num não existir devolve - "mes Invalido"



# print(mes_v4(12))


# Crie uma app permita registar um utilizador, use dicionários para representar o utilizador (nome e email)
# use uma função para fazer o registo

"""
def creat_user(nome:str, email:str):
    usrs = {"nome":nome.title(), "email":email.lower()}
    return usrs


nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

usr = creat_user(nome, email)

print(usr)

"""

# Crie uma app permita registar 5 utilizadores, use dicionários para representar o utilizador (nome e email)
# deve adicionar os utilizadores a uma lista
# use uma função para fazer o registo


def is_mail_valid(mail:str):
    return "@" in mail

def creat_user(id: int, nome:str, email:str):
    usrs = {"id": id, "nome":nome.title(), "email":email.lower()}
    return usrs

# ?
lista_usrs = []
# ?
for i in range(1, 3):
    print(f"-- User {i} --")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    if not is_mail_valid(email):
        print("Email invalido")
        continue

    print(f"-------------")
    usr = creat_user(i, nome, email)
    # ?
    lista_usrs.append(usr)


print(lista_usrs)


userslist = []
contador = 0