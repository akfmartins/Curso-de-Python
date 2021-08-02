"""
Escreva um programa que leia a velocidade de um carro:
Se ele ultrapassar 80km avise que foi multado;
A multa vai custar 7,00 reais para cada KM acima do limite;
"""
v = float(input("Qual a velocidade do carro?: "))
print(v)
if v > 80:
    print("Voce foi multado! ")
    multa = (v - 80) * 7
    print("A multa custara: {:.2f} ".format(multa))
else:
    print("Não ultrapasse a velocidade permitida!")

