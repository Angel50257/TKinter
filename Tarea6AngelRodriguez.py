"""1. Escribe una función llamada obtener_elemento que tome una lista y un índice como
argumentos, e intente devolver el elemento en la posición indicada de la lista. Si el
índice está fuera de rango, la función debe capturar la excepción y devolver el
mensaje "Error: Índice fuera de rango." """
from math import expm1


def obtener_elemento(lista,indice):
    try:
        return lista[indice]
    except IndexError:
        return "Error: Índice fuera de rango."

lista = [1,2,3,4,5]
#print(obtener_elemento(lista,3))
#print(obtener_elemento(lista,5))

"""2. Escribe una función llamada obtener_valor que tome un diccionario y una clave 
como argumentos, e intente devolver el valor asociado a la clave. Si la clave no existe 
en el diccionario, la función debe capturar la excepción y devolver el mensaje "Error: 
Clave no encontrada." """

def obtener_valor(diccionario,clave):
    try:
        return diccionario[clave]
    except KeyError:
        return "Error: Clave no encontrada."


diccionario = {"nombre":"angel",
               "apellido":"rodriguez"
               }
#print(obtener_valor(diccionario,"nombre"))
#print(obtener_valor(diccionario,"edad"))

"""3. Escribe una función llamada pedir_numero que solicite al usuario que ingrese un 
número. Si el usuario ingresa un valor no numérico, la función debe capturar la 
excepción y pedir nuevamente al usuario que ingrese un número. """
def pedir_numero():
    while True:
        try:
            n = int(input("Ingrese un numero entero: "))
            return n
        except ValueError:
            print("Error: Tipo de dato inapropiado")

#numero = pedir_numero()
#print(f"Número ingresado correctamente: {numero}")

"""4. Escribe una función llamada suma_lista que tome una lista como argumento y 
devuelva la suma de sus elementos. Si la lista contiene elementos no numéricos, la 
función debe capturar la excepción y devolver el mensaje "Error: La lista contiene 
elementos no numéricos." """
def suma_lista(lista):
    try:
        return sum(lista)
    except TypeError:
        return "Error: La lista contiene elementos no numéricos."

lista = [1,2,3,4]
#print(suma_lista(lista))
#print(suma_lista([1,2,3,'h']))

"""5. Escribe una función llamada acceder_elemento que tome un set y un elemento 
como argumentos, e intente verificar si el elemento está en el set. Si el set no es del 
tipo correcto, la función debe capturar la excepción y devolver el mensaje 
"Error: El primer argumento no es un set." """

def acceder_elemento(set,elemento):
    try:
        return elemento in set
    except TypeError:
        return "Error: El primer argumento no es un set."

set = {1,2,3,4}
#print(acceder_elemento(set,3))
#print(acceder_elemento(set,5))

"""6. Escribe una función llamada concatenar_cadenas que tome dos argumentos y 
devuelva su concatenación como una cadena. Si alguno de los argumentos no es una 
cadena, la función debe capturar la excepción y devolver el mensaje 
"Error: Ambos argumentos deben ser cadenas." """
def concatenar_cadenas(cadena1,cadena2):
    try:
        cadena = cadena1+cadena2
        return cadena
    except TypeError:
        return "Error: Ambos argumentos deben ser cadenas."
cadena1 = "Esta es una cadena de texto."
cadena2 = "Segunda cadena"

#print(concatenar_cadenas(cadena1,cadena2))
#print(concatenar_cadenas("Ejemplo 1",2))

"""7. Escribe una función llamada suma_numeros_lista que tome una lista de números 
como argumento y devuelva la suma de todos los números. Si la lista contiene 
elementos no numéricos, la función debe capturar la excepción y devolver el 
mensaje "Error: La lista contiene elementos no numéricos." """
def suma_numeros_lista(lista):
    try:
        return sum(lista)
    except TypeError:
        return "Error: La lista contiene elementos no numéricos."

lista = [1,2,3,4]
#print(suma_numeros_lista(lista))
#print(suma_numeros_lista([1,2,'h']))

"""8. Escribe una función llamada convertir_a_flotante que tome una cadena como 
argumento e intente convertirla a un número flotante. Si la cadena no puede ser 
convertida, la función debe capturar la excepción y devolver el mensaje 
"Error: No se puede convertir la cadena a un número flotante." """
def convertir_a_flotante(cadena):
    try:
        return float(cadena)
    except ValueError:
        return "Error: No se puede convertir la cadena a un número flotante."

cadena = "3.141516"
#print(convertir_a_flotante(cadena))
#print(convertir_a_flotante("El numero es: 3.141516"))

"""9. Escribe una función llamada calcular_factorial que tome un número entero no 
negativo como argumento y devuelva su factorial. Si el número es negativo, la 
función debe capturar la excepción y devolver el mensaje 
"Error: El número debe ser no negativo." """
def calcular_factorial(numero):
    try:
        if numero < 0:
            raise ValueError("Error: El número debe ser no negativo.")
        factorial = 1
        for i in range (1,numero+1):
            factorial*=i
        return factorial
    except ValueError as e:
        return str(e)

#print(calcular_factorial(3))
#print(calcular_factorial(-3))

"""10. Escribe una función llamada leer_y_sumar_enteros que tome un nombre de archivo 
como argumento, lea los números enteros en el archivo (un número por línea) y 
devuelva la suma de estos números. Si el archivo no existe o contiene valores no 
numéricos, la función debe capturar la excepción y devolver el mensaje 
"Error: Archivo no encontrado o contiene valores no numéricos." """
def leer_y_sumar_enteros(archivo):
    try:
        with open(archivo,"r") as archivo:
            return sum(int(linea.strip()) for linea in archivo)
    except FileNotFoundError:
        return "Error: Archivo no encontrado."
    except ValueError:
        return "Error: El archivo contiene valores no numéricos."

archivo = "C:/Users/Angel/Escritorio/python/leer_sumar.txt"
#print(leer_y_sumar_enteros(archivo))

"""11. Escribe una función llamada buscar_subcadena que tome una cadena y una 
subcadena como argumentos, e intente devolver el índice de la primera aparición 
de la subcadena en la cadena. Si la subcadena no se encuentra, la función debe 
capturar la excepción y devolver el mensaje "Error: Subcadena no encontrada." """
def buscar_subcadena(cadena, subcadena):
    try:
        indice = cadena.index(subcadena)
        return indice
    except ValueError:
        return "Error: Subcadena no encontrada."

print(buscar_subcadena("Angel Rodriguez","Rodriguez"))
print(buscar_subcadena("Diego Renato","Aguilar"))

