'''
Crie um algoritmo que leia seu numero e mostre seu dobro, seu triplo e a raiz quadrada.
'''

n = int(input("Digite um numero: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O dobro de {} vale {}, ".format(n, d))
print("O triplo de {} vale {}, \nA raiz quadra de {} é igual a {:.2f}, ".format(n, t, n, r))

