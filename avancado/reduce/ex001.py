# Desenvolva um programa que apresente o maior e o menor valores da sequência ([54, 10, 29, 87, 7, 64])

# reduce->usado para aplicar uma determinada funcao passada em seu argumento a todos os elementos da lista
from functools import reduce

numeros = [54, 10, 29, 87, 7, 64]
maior_valor = reduce(lambda n1, n2: n1 if n1 > n2 else n2,numeros)
menor_valor = reduce(lambda n1, n2: n1 if n1 < n2 else n2,numeros)
print(f'Lista: {numeros}')
print(f'Maior valor da lista: {maior_valor} e menor valor: {menor_valor}')