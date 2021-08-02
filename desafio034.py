"""
Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento;
Para salários superiores a R$ 1.250,00, calcular aumento de 10%;
Para salários inferiores ou iguais, calcular 15%;
"""
salario = float(input('Salário do colaborador: '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

print('Salario original: R$ ', salario)
print('Percentual: ',percentual,'%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento

print('Aumento: R$ ',aumento)
print('Novo salário: R$ ', novo_salario)
