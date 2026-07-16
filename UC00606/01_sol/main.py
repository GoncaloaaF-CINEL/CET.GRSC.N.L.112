"""

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.



Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9).




"""


print("----ex8----")
print("""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
""")

valor_hora = float(input("Informe o valor da hora: "))
num_horas = int(input("Informe a quantidade de horas trabalhadas: "))

salario_mes = valor_hora * num_horas

print(f"Este mes vais receber {salario_mes}€")

print("\n----ex9----")

print("""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9).
""")

temperatura_f = float(input("Indique uma temperatura em graus Fahrenheit: "))

temperatura_c = 5 * ((temperatura_f - 32) / 9)

print(f"{temperatura_f}ºF = {temperatura_c:.2f}ºC")