'''
Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
'''
salarioInicial = float(input("Qual seu salario?: "))
percentualAumento = float(input("Qual o percentual de aumento?: "))
percentualAumento2 = percentualAumento * salarioInicial / 100
salarioNew = salarioInicial + percentualAumento2
print("Seu salário atual é de: R$ ", salarioInicial)
print("Voce teve um aumento de: ", percentualAumento)
print("Seu novo salário é de: R$ ", salarioNew)
