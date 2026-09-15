"""

Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

"""

def ex1(n):
    for i in range(1, n+1):
        for j in range(i):
            print(f"{i:2}", end=" ")
        print()

