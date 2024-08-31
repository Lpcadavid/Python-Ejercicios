# 1 Eliminar duplicados de una lista:

def eliminar_duplicados(lista):   
    elementos_unicos = set()
    nueva_lista = []
    i = 0
    while i < len(lista):
        if lista[i] not in elementos_unicos:
            elementos_unicos.add(lista[i])
            nueva_lista.append(lista[i])
        i += 1
    return nueva_lista
 
lista_numeros = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(lista_numeros)
print(resultado)  

# 2 Adivinar un número con intentos limitados:
import random
 
numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7
adivinado = False
 
print("Estoy pensando en un número entre 1 y 100.")
while intentos < max_intentos and not adivinado:
    intento = int(input("Intenta adivinar el número: "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intentos.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es mayor que", intento)
    else:
        print("El número es menor que", intento)
 
if not adivinado:
    print("Lo siento, no adivinaste el número en el número máximo de intentos.")
    print("El número secreto era", numero_secreto)

   #3.Contar vocales en una frase

def contar_vocales(frase):    
    contador = 0
  
    vocales = "aeiouAEIOU"   
    i = 0
    
    while i < len(frase):  
        if frase[i] in vocales:
            contador += 1
      
        i += 1
 
    return contador 
frase_usuario = input("Ingresa una frase: ")
cantidad_vocales = contar_vocales(frase_usuario)
print(f"La frase contiene {cantidad_vocales} vocales.")

# 4 Calculadora básica:

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    while True:
        print("\nSelecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Ingresa tu opción (1/2/3/4/5): ")
        
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break
        
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {division(num1, num2)}")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
calculadora()

# 5 Lista Numeros Pares
def numeros_pares():
    contador = 1
    lista_pares = []   

    while contador <= 100:       
        if contador % 2 == 0:
            lista_pares.append(contador)
            contador += 1
    
    return lista_pares

resultado = numeros_pares()
print(resultado) 
 




