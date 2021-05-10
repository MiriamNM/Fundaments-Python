def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }
    # print(mi_diccionario)

    pobracion_paises = {
        'Argentina' : 1346345,
        'Mexico' : 24353465,
        'Colombia' : 435345,
    }
    # print(pobracion_paises['venezuala'])
    
    # for paises in pobracion_paises.keys():
    #     print(paises)

    # for paises in pobracion_paises.values():
    #     print(paises)

    for paises, poblacion in pobracion_paises.items():
        print(paises + ' tiene ' + str(poblacion) + ' habitantes')



if __name__ == '__main__':
    run()