# Desenvolva um programa que apresente a soma dos valores pares e dos valores ímpares da sequência ([21, 5, 34, 8, 16, 7, 3])

numeros = [21, 5, 34, 8, 16, 7, 3]
soma_impar = sum(map(lambda n: n if n%2 == 0 else 0, numeros))
soma_par = sum(map(lambda n: n if n%2 !=0 else 0, numeros))
print(f'Numeros: {numeros}')
print(f'A soma dos valores pares é {soma_par} e dos ímpares é {soma_impar}')