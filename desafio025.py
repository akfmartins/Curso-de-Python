'''
Crie um programa que leia o nome de uma pessoa e mostre se ela tem "SILVA" no nome.
'''

nome = str(input("Qual seu nome completo: ")).strip()
print("Seu nome tem SILVA {} ".format("SILVA" in nome))


