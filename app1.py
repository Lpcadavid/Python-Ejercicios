# 1. Sumar todos los elementos de una lista:

def suma_elementos(lista):

    suma = 0

    for numero in lista:

        suma += numero

    return suma


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"1. La suma de todos los elementos es: {suma_elementos(numeros)}")


# 2. Contar la cantidad de elementos pares en una lista:

def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cantidad_pares = contar_pares(numeros)
print(f"2. La cantidad de números pares es: {cantidad_pares}")


# 3. Encontrar el elemento más grande de una lista:

def elemento_mas_grande(lista):

    maximo = lista[0]

    for numero in lista:

        if numero > maximo:
            maximo = numero

    return maximo


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(
    f"3. El elemento más grande de la lista es: {elemento_mas_grande(numeros)}")


# 4. Crear una nueva lista con los elementos de otra lista multiplicados por 2:

def multiplicar_elementos(lista):

    nueva_lista = []

    for numero in lista:

        nueva_lista.append(numero * 2)

    return nueva_lista


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(
    f"4. La nueva lista con los elementos multiplicados por 2 es: {multiplicar_elementos(numeros)}")

# 5. Invertir una lista:


def invertir_lista(lista):

    nueva_lista = []

    for i in range(len(lista) - 1, -1, -1):

        nueva_lista.append(lista[i])

    return nueva_lista


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"5. La lista invertida es: {invertir_lista(numeros)}")

#

def eliminar_duplicados(lista):
    # Crear un conjunto para almacenar los elementos únicos
    elementos_unicos = set()
    # Crear una nueva lista para los resultados
    nueva_lista = []
    # Inicializar el índice
    i = 0
    # Usar un bucle while para recorrer la lista
    while i < len(lista):
        # Si el elemento no está en el conjunto, añadirlo
        if lista[i] not in elementos_unicos:
            elementos_unicos.add(lista[i])
            nueva_lista.append(lista[i])
        # Incrementar el índice
        i += 1
    return nueva_lista
 
# Ejemplo de uso
lista_numeros = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(lista_numeros)
print(resultado)  # Salida: [1, 2, 3, 4, 5]


