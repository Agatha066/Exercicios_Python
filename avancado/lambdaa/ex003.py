# Desenvolva uma calculadora rudimentar onde o usuário deve informar: qual operação ele deseja realizar, quais os valores para a realização do cálculo (apenas dois valores) e o resultado da operação
def menu():
    print('\n ### MENU ###\n\n\t (+) - Soma\n\t (-) - Subtração\n\t (/) - Divição\n\t (*) - Multiplicação\n\t (**) - Exponenciação')

def default():
    print('input invalido!')

def conta(a,b,opc):
    switch={
      '+': lambda a, b: a + b, #soma
      '-': lambda a, b: a - b, #subtacao
      '/': lambda a, b: a / b, #divisao
      '*': lambda a, b: a * b, #multiplicaçao
      '**': lambda a, b: a ** b, #exponenciação
      }
    if switch.get(opc):
      return switch.get(opc)(a,b)
    else:
      default()

menu()
opc = str(input('Informe a operação: \n'))

a = int(input('entre com o 1° valor: '))
b = int(input('Entre com o 2° valor: '))
print(f'\tResultado: {conta(a,b,opc)}\n')
