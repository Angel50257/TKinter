#1. Escribe una función en Python llamada sumar que reciba dos números y retorne su suma.
from ast import literal_eval
from multiprocessing.forkserver import read_signed
from os.path import split


def sumar():
   num1 = int(input("Ingrese el primer número: "))
   num2 = int(input("Ingrese el segundo número: "))
   resultado = num1 + num2
   print("La suma de ambos números es: ",resultado)
#sumar()

#2. Escribe una función en Python llamada es_par que reciba un número y retorne True si el número es par, y False en caso contrario.
def es_par():
    num = int(input("Ingrese un número: "))

    if num % 2 == 0:
        print("True") #return True
    else:
        print("False") #return False

#es_par()

#3. Escribe una función en Python llamada celsius_a_fahrenheit que reciba una temperatura en grados Celsius y la convierta a grados Fahrenheit.
# La fórmula de conversión es: F = C * 9/5 + 32.
def celsius_a_fahrenheit():
    celsius = float(input("Ingrese la temperatura en Celsius: "))

    fahrenheit = celsius * 9/5 +32
    print(f"Fahrenheit: {fahrenheit:.2f}")

#celsius_a_fahrenheit()

#4. Escribe una función en Python llamada maximo que reciba dos números y retorne el mayor de ellos.
def maximo():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if num1 > num2:
        print(f"EL número mayor es: {num1}")
    elif num2 > num1:
        print(f"EL número mayor es: {num2}")
    else:
        print("Ambos números son iguales.")

#maximo()

#5. Escribe una función en Python llamada contar_caracteres que reciba una cadena de texto y retorne el número de caracteres que contiene.
def contar_caracteres():
    cadena = (input("Ingrese la cadena de texto: "))
    nueva_cadena = []
    contar = 0
    caracter = 0

    for i in cadena:
        contar+=len(i)
        nueva_cadena.append(contar)
        caracter = max(nueva_cadena)
    print(f"El número de caracteres que contiene la cadena es de: {caracter}")

#contar_caracteres()

#6. Escribe una función en Python llamada cuadrado que reciba un número y retorne su cuadrado.
def cuadrado():
    num = int(input("Ingrese un número: "))

    cuadrado = (num * num)
    print(f"El cuadrado de {num} es: {cuadrado} ")

#cuadrado()

#7. Escribe una función en Python llamada minutos_a_segundos que reciba un número de minutos y los convierta a segundos.
def minutos_a_segundos():

    minuto = float(input("Ingrese los minutos: "))

    min = 60#segundos
    resultado = minuto * min
    print(f"{minuto} minuto(s) equivalen a {resultado} segundo(s)")

#minutos_a_segundos()

#8. Escribe una función en Python llamada longitud_lista que reciba una lista y retorne su longitud.
def longitud_lista():
    lista = (input("Ingrese caracteres para crear una lista: "))
    longitud = 0
    longitud = len(lista.split())
    print("La lista es:",lista.split())
    print("La longitud de la lista es: ",longitud)

#longitud_lista()

#9. Escribe una función en Python llamada es_minusculas que reciba una cadena de texto y retorne True si la cadena está en minúsculas, y False en caso contrario.
def es_minusculas():
    cadena = (input("Ingrese una cadena de texto: "))

    minuscula = cadena.lower()

    if cadena == minuscula:
        print("True")
    else:
        print("False")

#es_minusculas()

#10. Escribe una función en Python llamada contar_vocales que reciba una cadena de texto y retorne el número de vocales que contiene.
def contar_vocales():
    cadena = input("Ingresa una cadena de texto: ").lower()
    contador = 0

    vocales = ("a","e","i","o","u")

    for i in cadena:
        if i in vocales:
            contador+=1
    print(f"En la cadena hay {contador} vocales")

#contar_vocales()

#11. Escribe una función en Python llamada area_circulo que reciba el radio de un círculo y retorne su área. Usa la fórmula: área = π * radio^2.
def area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))

    area = 3.1416 * pow(radio,2)
    print(f"El área del círculo es: {area:.2f}",)

#area_circulo()

#12. Escribe una función en Python llamada convertir_mayusculas que reciba una lista de cadenas y retorne una nueva lista con todas las cadenas en mayúsculas.
def convertir_mayusculas():
    contador = int(input("Cuantas cadenas necesita: "))
    cadena_total = []

    for i in range(0,contador):
        lista = (input("Escribe una cadena: "))
        cadena_total.append(lista.upper())

    print(f"Las cadenas en mayusculas son: {cadena_total}")

#convertir_mayusculas()

#13. Escribe una función en Python llamada numero_mas_pequeno que reciba una lista de números y retorne el número más pequeño de la lista.
def numero_mas_pequeno():
    lista = (input("Ingrese una lista de números: "))

    nueva_lista = list(map(int, lista.split()))
    resultado = min(nueva_lista)
    print("El número más pequeño en la lista es:", resultado)

#numero_mas_pequeno()

#14. Escribe una función en Python llamada concatenar_listas que reciba dos listas y retorne una nueva lista que sea la concatenación de las dos.
def concatenar_listas():
    lista1 = (input("Ingresa datos de la lista 1: "))
    lista2 = (input("Ingresa datos de la lista 2: "))

    lista = lista1+" "+lista2
    print(lista)

#concatenar_listas()

#15. Escribe una función en Python llamada contar_palabras que reciba una frase (cadena de texto) y retorne el número de palabras que contiene.
def contar_palabras():
    cadena = input("Ingresa una cadena de texto: ")

    palabra = cadena.split()
    contar = len(palabra)
    print(f"En la cadena hay {contar} palabras")

#contar_palabras()

#16. Escribe una función en Python llamada promedio que reciba una lista de números y retorne su promedio.
def promedio():
    lista = (input("Ingrese una lista de números: "))
    nueva_lista = []

    division = lista.split()
    nueva_lista = map(int, lista.split())
    resultado = sum(nueva_lista)/len(division)
    print("El promedio de la lista es:",resultado)

#promedio()

#17. Escribe una función en Python llamada sumar_lista que reciba una lista de números y retorne la suma de todos sus elementos.
def sumar_lista():
    lista = (input("Ingrese una lista de números: "))

    nueva_lista = list(map(int, lista.split()))
    resultado = sum(nueva_lista)
    print("La suma total de los números en la lista es:",resultado)

#sumar_lista()

#18. Escribe una función en Python llamada maximo_lista que reciba una lista de números y retorne el número máximo de la lista.
def maximo_lista():
    lista = (input("Ingrese una lista de números: "))

    nueva_lista = list(map(int, lista.split()))
    resultado = max(nueva_lista)
    print("El número máximo en la lista es:",resultado)

#maximo_lista()

#19. Escribe una función en Python llamada multiplicar_lista que reciba una lista de números y retorne el producto de todos sus elementos.
def multiplicar_lista():
    lista = (input("Ingrese una lista de números: "))
    contador = 1

    nueva_lista = list(map(int,lista.split()))
    for i in nueva_lista:
        contador*=i

    print("El producto de la lista es:", contador)

#multiplicar_lista()

#20. Escribe una función en Python llamada sumar_matrices que reciba dos matrices del mismo tamaño y retorne una nueva matriz que sea la suma de las dos matrices.
#def sumar_matrices():

#sumar_matrices()

#21. Escribe una función en Python llamada multiplicar_matrices que reciba dos matrices y retorne una nueva matriz que sea el producto de las dos matrices.
#def multiplicar_matrices():

#multiplicar_matrices()

#22. Escribe una función en Python llamada suma_filas que reciba una matriz y retorne una lista con la suma de los elementos de cada fila.
#def suma_filas():

#suma_filas()

#23. Escribe una función en Python llamada suma_columnas que reciba una matriz y retorne una lista con la suma de los elementos de cada columna.
#def suma_columnas():

#suma_columnas()

#24. Escribe una función en Python llamada contar_ceros que reciba una matriz y retorne el número de ceros que contiene.
#def contar_ceros():

#contar_ceros()

#25. Escribe una función en Python llamada es simétrica que reciba una matriz cuadrada y retorne True si la matriz es simétrica, y False en caso contrario.
#Una matriz es simétrica si es igual a su transpuesta.
#def simetrica():

#simetrica()