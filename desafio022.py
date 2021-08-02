'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas;
O nome com todas as letras minúsculas;
Quantas letras ao todo sem considerar espaços;
Quantas letras tem o primeiro nome;
'''


nome = str(input("Qual é seu nome completeo?: ")).strip()   #eliminar os espaços antes e depois das frases
print("Analisando seu nome... ")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculo é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras ".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras ".format(nome.find(" ")))

