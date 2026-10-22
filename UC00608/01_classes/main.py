from Carro import Carro

c1 = Carro("BMW", "M5", 2025)
print(c1.marca, c1.modelo)


c2 = Carro("Ford", "Mustang", 2026)
print(c2.marca, c2.modelo)


# Criar um Fiat Punto de 2000
c3 = Carro("Fiat", "Punto", 2000)

# Mostrar a msg "Fiat Punto de 2000"
print(c3.get_info())

# altere o ano do Fiat para 2002

c3.ano = 2002

#mostre novamente a msg

print(c3.get_info())

c1.show_info()
c2.show_info()
c3.show_info()


c3.mudar_ano(2031)
c3.show_info()
