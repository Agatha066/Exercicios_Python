# Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar

numero = int(input('Digite um valor: '))

if numero%2==0:
    print(f'O nuemro {numero} e par!\n')
else:
    print(f'O numero {numero} é impar!\n')