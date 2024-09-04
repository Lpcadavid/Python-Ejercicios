
alumnos_notas = {}

while True:
    nombre = input("Introduce el nombre del alumno (o escribe 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    
    while True:
        try:
            nota = float(input(f"Introduce la nota de {nombre}: "))
            break
        except ValueError:
            print("Por favor, introduce la nota.")
    
    alumnos_notas[nombre] = nota

print("\nAlumnos y sus notas:")
for nombre, nota in alumnos_notas.items():
    print(f"{nombre}: {nota}")
    
    

def promedio_notas(diccionario):
    if not diccionario:
        return 0

   
    suma_notas = sum(diccionario.values())
    promedio = suma_notas / len(diccionario)

    return promedio

alumnos_notas = {
    'Lina': 8.5,
    'Carol': 9.0,
    'Jose': 7.5,
    'Andres': 6.0,
    'Gary': 7.0,
    'Mia': 6.8
}

promedio = promedio_notas(alumnos_notas)
print(f"El promedio de las notas es: {promedio:.2f}")

def alumno_con_mejor_nota(diccionario):
    if not diccionario:
        return None

  
    mejor_alumno = None
    mejor_nota = float('-inf') 

    for alumno, nota in diccionario.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno

    return mejor_alumno


alumnos_notas = {
    'Lina': 8.5,
    'Andres': 9.0,
    'Jose': 7.5,
    'Carol': 8.0
}


mejor_alumno = alumno_con_mejor_nota(alumnos_notas)
if mejor_alumno:
    print(f"El alumno con la nota más alta es: {mejor_alumno}")
else:
    print("No hay alumnos en el diccionario.")
    

def agregar_palabras():
    diccionario = {}

    while True:
        palabra = input("Introduce una palabra (o escribe 'salir' para terminar): ")
        
        if palabra.lower() == 'salir':
            break
        
        definicion = input(f"Introduce la definición de '{palabra}': ")
        
        diccionario[palabra] = definicion

    return diccionario

diccionario_palabras = agregar_palabras()

print("\nDiccionario de palabras y definiciones:")
for palabra, definicion in diccionario_palabras.items():
    print(f"{palabra}: {definicion}")
    
    
def buscar_palabra(diccionario, palabra):
    definicion = diccionario.get(palabra)
    
    if definicion:
        return definicion
    else:
        return "La palabra no se encontró en el diccionario."

diccionario_palabras = {
    'Serendipia': 'Hallazgo valioso que se produce de manera accidental o casual.',
    'Alborada': 'La palabra "albor" captura la efímera magia del sol emergiendo en el horizonte, tejiendo el cielo con tonos vibrantes.',
    'Armonia': 'es una palabra perfecta para definir todo aquello que funciona, ya sea en términos musicales o en el universo, en nuestras vidas.',
}

palabra_buscar = input("Introduce la palabra que deseas buscar: ")

resultado = buscar_palabra(diccionario_palabras, palabra_buscar)
print(f"Definición de '{palabra_buscar}': {resultado}")
    


