"""
Desenvolva um programa que pergunte a distancia de uma viagem em KM. 
Calcule o preço da passagem , cobrando R$ 0,50 por KM para cada viagem de até 200KM e 0,45
para viagens mais longas.
"""
distancia = float(input("Qual a distância da sua viagem? "))

print("Você está prestes a começar uma viagem de {:.1f}Km.".format(distancia))
print("E o preço da sua viagem será de R${:.2f}".format(distancia*0.5 if distancia <= 200 else distancia*0.45))