
ls = [1,2,3]
tp = (1, 2, 3) ## tuplo <-- ESTÁTICO
tp2 = (1, 2, 3)


print(tp)
print(tp[0])

tp3 = tp + tp2
print(tp3)


infos = ("Ana", "UC00606", 5)

nome, modulo, nota = infos

print(nome)
print(modulo)
print(nota)



infos = ["Ana", "UC00606", 5]

nome, modulo, nota = infos

print(nome)
print(modulo)
print(nota)



infos = ("Ana", "UC00606", 5)

print("-------")

for i in infos:
    print(i)


