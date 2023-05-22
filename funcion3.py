#  Crear una función que se llame ordenarCaracteres que reciba
# una cadena de caracteres como parámetro  y su responsabilidad 
# es ordenar los caracteres de manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenarCaracteres (cadena:str)->str:
    """_summary_
    Recibe un string y ordena sus caracteres de forma ascendente 
    Args:
        cadena (str): el string que quiere ordenarse

    Returns:
        str: el string ordenado
    """
    lista = list(cadena)

    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if lista[i] > lista[j]:  
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    cadena_ordenada = "".join(lista)

    return cadena_ordenada


cadena = "algoritmo"

print (ordenarCaracteres(cadena))