'''
Faça um programa que leia um numero de 0 a 9999 e mostre na tela
cada um dos dígitos separados.
'''

n = int(input("Escreva um numero de 4 dígitos: "))
u = (n // 1) % 10
print("O digito da unidade é: {}".format(u))
d = (n // 10) % 10
print ("O dígito das dezenas e: {}".format(d))
c = (n // 100) % 10
print("O dígito das centenas é: {}".format(c))
m = (n // 1000) % 10
print("O dígito milhar é: {}".format(m))
