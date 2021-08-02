'''
print('=====DESAFIO 20=====')
print('O mesmo professor quer sortear a orde de apresentação de trabalho dos alunos, faça um programa que mostre o nome dos\nquatro alunos e mostre a ordem sorteada.')
'''
import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)
