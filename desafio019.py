'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um progra que ajude ele, leia o nome deles e escreva o nome escolhido.
'''
import random
a1 = str(input("Nome do primeiro aluno: "))
a2 = str(input("Nome do segundo aluno: "))
a3 = str(input("Nome do terceiro aluno: "))
a4 = str(input("Nome do quarto aluno: "))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print("O Aluno escolhido foi {} ".format(escolhido))
print("Parabens!!! {} ".format(escolhido))



