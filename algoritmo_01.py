lista_de_numeros_01 = [1,4,2,250,14,27,21,7,-10,-25000]
lista_de_numeros_02 = [11,24,21,35,345,27,13,7,-25]


def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()
    nova_lista_de_numeros.sort()

    # for i in range(len(lista_de_numeros)):
    #     for j in range(i+1,len(nova_lista_de_numeros)):
    #         if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
    #             nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]
    
    return nova_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros_02)
