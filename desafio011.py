'''
Faça um programa que leia a altura e a largura de uma parede em metros, 
calcule a sua area e a quantidade de tinta necessaria para pinta-la.
Sabendo que cada litro de tinta pinta uma area de 2m2
'''

alt = float(input("Qual a altura da parede?: "))
larg = float(input("Qual a largura da parede?: "))
area = alt * larg
qTinta = area / 2

print("A parede: ", area, "Metros Quadrados")
print("A quantidade de tinta necessaria é:", qTinta, "Litros")

