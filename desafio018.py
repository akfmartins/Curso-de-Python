'''
Faça um programa que leia um angulo qualquer e mostre na tela o valor do:
Seno, Cosseno, Tangente desse angulo.
'''
import math

a = float(input("Digite o ângulo que você deseja: "))
print("Seno: {:.2f}".format(math.sin(math.radians(a))))
print("Cosseno: {:.2f}".format(math.cos(math.radians(a))))
print("Tangente: {:.2f}".format(math.tan(math.radians(a))))