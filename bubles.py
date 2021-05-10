# constador = 0
# print('2 elevado a ' + str(constador) + 'es igual a: ' + str(2**constador))

# constador = 2
# print('2 elevado a ' + str(constador) + 'es igual a: ' + str(2**constador))

# constador = 5
# print('2 elevado a ' + str(constador) + 'es igual a: ' + str(2**constador))

def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + 'es igual a: ' + str(2**potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()