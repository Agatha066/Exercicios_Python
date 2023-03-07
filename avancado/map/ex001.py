# Desenvolva um programa que converta todas as temperaturas desta lista em Celsius ([22.5, 40, 13, 29, 34]) para Fahrenheit

#Celsius = [22.5, 40, 13, 29, 34]
#contador = 1

#while contador > len(Celsius):
    #Fahrenheit = Celsius[contador]*1.8+32
    #contador+=1
    #print(f'Celsius: {Celsius[contador]} - Fahrenheit: {Fahrenheit}')

# round -> retorna um numero de apenas duas casas decimais

temperaturas_celsius = [22.5, 40, 13, 29, 34]
temperaturas_fahrenheit = list(map(lambda temp: round(1.8 * temp + 32, 1), temperaturas_celsius))
print(f'Temperaturas em celsius: {temperaturas_celsius}')
print(f'Temperaturas em fahrenheit: {temperaturas_fahrenheit}')