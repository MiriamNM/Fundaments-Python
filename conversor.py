def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantós pesos ' +tipo_pesos + ' tienes?:')
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares= round(dolares, 2)
    dolares= str(dolares)
    print('Tienes $ ' + dolares + ' dólares')


menu = """"
Bienvenido al conversor de monedas 

1- Pesos colombianos
2- Pesos argentinos
3- peros mexicanos

Elegir una opción:"""

opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('argentinos', 65)
elif opcion == 3:
    conversor(mexicanos, 20.24)
else :
    print('Ingresa una opción correcta por favor')


# pesos = input('¿Cuantós pesos colombianos tienes?:')
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares= round(dolares, 2)
# dolares= str(dolares)
# print('tienes $' + dolares + ' dolares')

# pesos = input('¿Cuantós pesos mexicanos tienes?:')
# pesos = float(pesos)
# valor_dolar = 20.24
# dolares = pesos / valor_dolar
# dolares= round(dolares, 2)
# dolares= str(dolares)
# print('tienes $' + dolares + ' dolares')

# dolares = input('¿Cuantós dolares tienes?:')
# dolares = float(dolares)
# valor_peso = 0.049
# pesos = pesos * valor_dolar
# pesos= round(pesos, 2)
# pesos= str(pesos)
# print('tienes $' + pesos + ' pesos')


