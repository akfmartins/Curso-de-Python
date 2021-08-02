'''
Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela
sua porção inteira.
'''

import math
num = float(input("Digite um numero real: "))
print("O Numero {} tem a parte inteira {}".format(num, math.trunc(num)))
