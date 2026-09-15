#          0        1        2
from time import process_time_ns

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