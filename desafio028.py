"""
Escreva um programa que faça o computador pensar em um numero entre 0 e 5;
e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador;
O programa deve escrever na tela se o usuário venceu ou perdeu;
"""
from random import randint
num = randint(0,5)
print("")
print("Vou sortear um numero de 0 a 5")
print("")
usuario = int(input("Qual será o numero?: "))
if usuario == num:
    print("Parabéns você acertou!!")
else:
    print("Você errou, o numero era {} ".format(num))
    
