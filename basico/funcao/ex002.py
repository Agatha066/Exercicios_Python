# Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

def numero_par_ou_impar(numero):
    return numero % 2 == 0

numero = int(input('Informe um número inteiro qualquer: '))

if numero_par_ou_impar(numero):
    print(f'O número {numero} é par')
else:  
    print(f'O número {numero} é impar')