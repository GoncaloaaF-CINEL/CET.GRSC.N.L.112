import sys

my_set = {"val1", "val2", "val3", "val4"}

print(sys.getsizeof(my_set))
print(my_set)

my_set.add("val5")
print(my_set)


my_set.add("val5")
print(my_set)

my_set.remove("val5")
print(my_set)

my_set.add("val5")
print(my_set)

my_set.discard("val5")
print(my_set)

# my_set.remove("val5") ## se não existir --> Erro
print(my_set)

my_set.discard("val5") ## se não existir --> NÃO da Erro
print(my_set)

for nome in my_set:
    print(nome)


print(my_set.__contains__("val1"))

my_set.update(("V1", "V2", "V3", "V4", "V5", "V6"))

print(my_set)


print("V1" in my_set)

print(sys.getsizeof(my_set))

my_set.clear()
print(my_set)

print(sys.getsizeof(my_set))
del my_set



my_set = {"val1", "val2", "val3", "val4"}

my_set2 = {"val2", "val3", "val5", "val6"}
my_set3 = {"val1", "val2"}


print(my_set.union(my_set2))

print(my_set.difference(my_set2))
print(my_set2.difference(my_set))

print(my_set.intersection(my_set2))

print(my_set.symmetric_difference(my_set2))

print(my_set.issubset(my_set2))

print(my_set3.issubset(my_set))
print(my_set.issuperset(my_set3))



my_set4 = {"A", "B", "val1"}
print(my_set.isdisjoint(my_set4))





"""
turma 1 - Ana, Rita, Joana
turma 2 - Joana, Luis, Pedro
turma 3 - Marta, Maria , Rita 
"""
