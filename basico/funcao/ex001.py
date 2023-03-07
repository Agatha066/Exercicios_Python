# Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

def numeros_par_ou_impar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    return f'O número {numero} é impar'

numero = int(input('Informe um número inteiro qualquer: '))
print(numeros_par_ou_impar(numero))