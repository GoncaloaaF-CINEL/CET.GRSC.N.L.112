from mypyc import primitives

Aeroportos = {
    "LIS":["Lisboa", "Figo maduro", "Ota"],
    "OPO": "Porto",
    "FAR": "Fro"
}


print(Aeroportos)
print(Aeroportos["LIS"])

print(Aeroportos["FAR"])

Aeroportos["FAR"] = "Faro"


Aeroportos["LHR"] = " London Heathrow"

print(Aeroportos)

#del Aeroportos["LHR"]

# Aeroportos.pop("LIS") ## remove o indicado
print(Aeroportos)


Aeroportos.popitem() ## remove o ultimo
print(Aeroportos)

# print(Aeroportos["LGW"])
print(Aeroportos.get("FAR", "Código invalido"))


print(Aeroportos.keys())
print(Aeroportos.values())
print(Aeroportos.items())

print("------")
for bananas, lisboa in Aeroportos.items():
    print(f"{bananas}: {lisboa}")
print("------")
for v in Aeroportos.items():
    print(f"{v[0]}: {v[1]}")

print("------")
for v in Aeroportos: # iterar pela key
    print(v)

print("------")
for v in Aeroportos.keys(): # iterar pela key
    print(v)

print("------")
for v in Aeroportos.values(): # iterar pela key
    print(v)

print("------")
for v in Aeroportos.keys(): # iterar pela key
    print(Aeroportos[v])


print(Aeroportos["LIS"][1])