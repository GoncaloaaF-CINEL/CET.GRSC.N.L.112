#          0        1        2
from time import process_time_ns

from mypyc import primitives

nomes = ["João", "Carlos", "Rui"]

print(nomes)

print(nomes[1])

nomes[1] = "Maria"
print(nomes)

nomes.append("Luisa")
#            -4       -3     -2        -1
#            0         1       2        3
# nomes = ["João", "Carlos", "Rui", "Luisa"]
print(nomes)


print(nomes[0])

print(nomes[3])
print(nomes[-1])


print(nomes[0])
print(nomes[-4])

nomes.append("Julia")
print(nomes)

"""
nome1, nome2, nome3
nome1, nome2, nome3, nome4
nome0 ,nome1,nome2 ,nome3 , nome4
"""

nomes.insert(2, "Diana")
print(nomes)


print(nomes.__len__())
print(len(nomes))

print(nomes.__contains__("Diana"))
print("Diana" in nomes)

nomes.remove("Diana")
print(nomes)

nomes.append("João")
print(nomes)


nomes.remove("João")
print(nomes)

nomes.pop(2)
print(nomes)

print(nomes.append("João2"))

print(nomes.remove("João2"))
print(nomes.pop(-1))


print("--" * 10)
print(nomes)
# itr listas

for nome in nomes:
    print(nome.upper())

print("--" * 5)
i = 0
while i < len(nomes):
    print(nomes[i])
    i += 1

print("-" * 5)

i = 0
while i < len(nomes):
    print(f"{i}: {nomes[i]}")
    i += 1


print("-" * 5)
nomes.append("Rui")

for idx, nome in enumerate(nomes, start=1):
    print(f"{idx}: {nome}")

print("-" * 5)

curr_idx = 0
for nome in nomes:
    print(f"{nomes.index(nome, curr_idx)+1}:{nome}")
    curr_idx += 1

print("-" * 5)


# aceder v2

nomes = [
    "João Silva", "Maria Santos", "Pedro Ferreira", "Ana Costa", "Miguel Oliveira",
    "Sofia Rodrigues", "Tiago Martins", "Inês Sousa", "André Pereira", "Beatriz Almeida",
    "Ricardo Gomes", "Mariana Lopes", "Bruno Carvalho", "Carolina Ribeiro", "Diogo Teixeira",
    "Catarina Correia", "Rui Fernandes", "Marta Marques", "Gonçalo Moreira", "Daniela Cardoso",
    "Nuno Rocha", "Patrícia Neves", "Fábio Pinto", "Sara Monteiro", "Hugo Nunes",
    "Cláudia Vieira", "Luís Coelho", "Joana Mendes", "Vasco Ramos", "Filipa Castro",
    "Eduardo Barbosa", "Cristiana Reis", "Marco Tavares", "Diana Matos", "Paulo Cunha",
    "Raquel Faria", "Alexandre Simões", "Rita Azevedo", "David Fonseca", "Susana Baptista",
    "Carlos Pires", "Mónica Leal", "Jorge Antunes", "Helena Machado", "Samuel Freitas",
    "Teresa Campos", "Nelson Duarte", "Andreia Correia", "Márcio Henriques", "Liliana Brito"
]

print(len(nomes))

print(nomes[0:6]) # nomes[0:6] -> lista com todos elm da lista original das pos 0 are a 6-1

print(nomes[4:6])


print(nomes[:6])
print(nomes[45:-1])

print(nomes[-8:-1])
print(nomes[-8:])
print(nomes[-30:40]) # evito isto


print(nomes[5:40])
print(nomes[5:40:5])

#       start : end : step
print(nomes[-1:-20:-5])



print("-------------------------")
# listComp


lst = []
for nome in nomes:
    if "q" in nome:
        lst.append(len(nome))

print(lst)

# newlist = [expression for item in iterable if condition == True]
lst2 = [len(nome) for nome in nomes if "q" in nome]

print(lst2)