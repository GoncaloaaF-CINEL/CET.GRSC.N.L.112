"""
4. Supondo que a população de um país
A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
 que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.


 Faça um programa que calcule e escreva o número de anos necessários para que a população do país
  A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""

"""
País A

ano 0   10  3%
ano 1   13  3%
ano 2   84_872  3%   

País B

ano 0   20      1,5%
ano 1   20,3    1,5%
ano 2   206_045 1,5%

"""


"""
Faça um Programa que peça um número e então mostre a mensagem 
 -> O número informado foi [número].
"""

num = int(input("digite um número: "))
print(f"O número informado foi {num}")
print("O número informado foi {}".format(num))
print("O número informado foi", num)
print("O número informado foi " + str(num))


"""
faça um programa que mostre a msg "ola mundo" 10 vezes 
"""

"""
Crie uma app que peça ao utilizador números, quando o utilizador inserir 0 termine o Programa 
Crie uma app que peça ao utilizador 10 números
"""

popA = 80000
taxaA = 1.03

popB = 200000
taxaB = 0.015

ano = 0

while popA <= popB:
    popA = popA * taxaA
    popB = popB + (popB * taxaB)

    ano += 1

print(f"O país A supera o B em {ano} anos")


#.....
print("Ola Mundo")
