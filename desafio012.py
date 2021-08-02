'''
Faça um algotitmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
'''

valorOriginal = float(input("Qual o valor do produto?: R$ "))
desconto = float(input('Entre com o percentual do desconto: '))
desconto2 = desconto * valorOriginal / 100
valorFinal = valorOriginal - desconto2
print("O valor real do produto: ", valorOriginal)
print("O valor do desconto: ", desconto2)
print("Valor com desconto: ", valorFinal)

