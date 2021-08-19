from random import randint
from time import sleep
itens = ("Pedra", "Papel","Tesoura")
computador = randint(0,2)
print("""SUAS OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")
você = int(input("Qual sua jogada?: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-=" * 12)
print("O Computador jogou: {}".format(itens[computador]))
print("Voce jogou: {}".format(itens[você]))
print("-=" * 12)
if computador == 0:
    if você == 0:
        print("HOUVE EMPATE!")
    elif você == 1:
        print("Você Ganhou!")
    elif você == 2:
        print("O Computador Venceu!")
    else:
        print("JOGADA INVÁLIDA!")
if computador == 1:
    if você == 0:
        print("O Computador Venceu!")
    elif você == 1:
        print("Houve Empate!")
    elif você == 2:
        print("Você Venceu!")
    else:
        print("JOGADA INVÁLIDA!")
if computador == 2:
    if você == 0:
        print("Você Venceu!")
    elif você == 1:
        print("O Computador Venceu!")
    elif você == 2:
        print("Houve Empate!")
    else:
        print("JOGADA INVÁLIDA!")



