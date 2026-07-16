# condições
"""

==
!=

>
<
>=
<=

"""
import random
from unittest import case

idade = 19

if idade >= 18:
    print("Adulto")
elif idade >= 12: # <- sei q tem menos de 18
    print("Teen")
else:
    print("Kid")

print("-------- And --------")
a = 50
b = 20
c = 30

if a > b and a > c:
    print("A")
else:
    print("Não A")


print("-------- or --------")
a = 25
b = 20
c = 30

if a > b or a > c:
    print("A")
else:
    print("Não A")




print("-------- Not --------")
a = 16
b = 20
c = 30

if not (a > b) or a > c:
    print("A")
else:
    print("Não A")




print("-------- And --------")

a = 20
b = 20
c = 30
print(a > b)
print(a > c)
print(a > c and a > c)

print("-------- or --------")
a = 25
b = 20
c = 30
print(a > b)
print(a > c)
print(a > c or a > b)

print("-------- not --------")


a = 20
b = 20
c = 30
print(not (a > b))
print(a > c)


print(not ( (a > c) and (a > b) )  )


# match

mes = 1

if mes == 1:
    print("Jan")
elif mes == 2:
    print("Feb")
elif mes == 3:
    print("Mar")
elif mes == 4:
    print("Apr")
elif mes == 5:
    print("May")
elif mes == 6:
    print("Jun")
else:
    print("mes invalido")

mes = 3
match mes: # switch/case
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("Apr")
    case 5:
        print("May")
    case 6:
        print("Jun")
    case _:
        print("mes invalido")

# range

range(5) # 0 a 4, -> range(n) tem todos os num int de 0 a n-1

range(5, 10) # 5 a 9, -> range(m,n) tem todos os num int de m a n-1
range(0, 5) # = range(5)

range(0, 10, 2) # 0 a 9 de 2 em 2 (0, 2, 4, 6, 8) -> range(m,n,s ) tem todos os num int de m a n-1 com step de s

# loops

for elm in range(5, 100, 5):
    print(elm, end=" ")

print("")
print("--" * 10)

print("")
for elm in range(5, 100, 5):
    if elm == 50:
        break # termina o loop (for) (salta para a linha 153)

    if elm % 2 == 0:
        print("par", end=" ")
        continue

    print(elm, end=" ")


# while

print()
max = 10
min = 0
while max >=  min:
    print(min, end=" ")
    min += 1

contador = 0
while True:

    contador += 1
    print(contador)

    num  = random.randint(1, 10000)
    if num == 726:
        break



# ex