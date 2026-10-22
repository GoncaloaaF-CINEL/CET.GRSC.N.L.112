import random

random.randint(0, 100)

# Crie a app Guess the Number, deve usar funções


def gerar_num_random(min_val:int = 0, max_val:int = 100):
    return random.randint(min_val, max_val)

def validar_respota(target:int, guess:int):
    if guess == target:
        return True, "Acertou"
    elif guess < target:
        return False, "Errou, o target e menor"
    else:
        return False, "Errou, o target é maior"

def partida(min_val:int = 0, max_val:int = 100):

    num_secreto = gerar_num_random(min_val, max_val)
    print(num_secreto)
    num_tentativas = 0
    while True:
        num_tentativas += 1
        guess = input(f"Digite um numero entre {min_val} e {max_val}: ")

        if not guess.isnumeric():
            print("entrada invalida")
            continue

        guess = int(guess)

        resp = validar_respota(guess, num_secreto)

        print(resp[1])

        if resp[0]:
            break

    return num_tentativas





def jogo(min_val:int = 0, max_val:int = 100):
    ranking = []

    for n in range(0, 2):
        num_tetativas = partida(min_val, max_val)
        ranking.append(num_tetativas)

    ranking.sort()
    print(ranking)


jogo(min_val = 0, max_val = 10)

# Crie a app Guess the Number, deve usar funções
    # gerar um num (target)
    # pedir num ao usr
    # ver se o input e valido
    # verificar a resposta
        # se num > target  -> informar que o target e menor
        #    - Voltar a pedir o num
        # se num < target  -> informar que o target e maior
        #    - Voltar a pedir o num
        # se num ==  target  -> informar esta correto






# conte o número de tentativas
# mostre o ranking dos 5 melhores jogadores


