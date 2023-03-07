# Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar

numero = int(input('entre com um numero: '))

x = lambda numero: numero % 2 == 0

if x(numero):
    print(f'O numero {numero} é par\n')
else:
    print(f'O numero {numero} é impar\n')