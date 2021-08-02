'''
escreva um programa que leia o valor em metros e o exiba convertido em cm e mm.
'''
km = float(input("Quantos Km?: "))
m = float(km * 1000)
cm = int(m * 100)
mm = int(m * 1000)
print("O valor de entrada é: {} , em m {},  em cm é: {}, e em mm {} ".format(km, m,cm, mm))