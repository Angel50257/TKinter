"""
#Manejo de excpeciones try

#Ejemplo 1
#Try-Except Block
try:
    #Código que puede lanzar una excepción
    resultado =10/0
except ZeroDivisionError:
#Manejo de la excepción
    print("Error: No se puede dividir por cero")

#===============================================================
#Ejemplo 2
try:
    with open("C:/Users/PC-DEV15/Documents/Ejemplo.txt","r") as archivo:
        contenido= archivo.read()
        print(contenido)
        archivo.close()
except FileNotFoundError:
    print("El archivo no existe, verifique el nombre")
#===============================================================

#Ejemplo 3
#Múltiples bloques
try:
    resultado =10/0
except ValueError:
    print("Error: Valor no válido.")
except ZeroDivisionError:

    print("Error: No se puede dividir por cero")

#=============================================================================
#Ejemplo 4
def manejar_errores():
    try:
        diccionario={"a":1,"b":2} #Crear diccionario
        x = diccionario["C"] #asignamos un valor a encontrar en el didccionario
        print(x) #este esté o no queda igual porque no existe C como tal en el diccionario jajaja
    except ValueError:
        print("Error: No se puede convertir la cadena a un número entero")
    except TypeError:
        print("Error: Tipo de dato inapropiado")
    except KeyError:
        print("Clave no encontrada en el diccionario")

manejar_errores()

"""
#============================================================================
#Ejemplo 5
def manejar_errores():
    try:
        opcion=int(input("Elige un error\n (1: ValueError\n 2: TypeError\n 3: KeyError): "))

        if opcion ==1:
            x=int("10/5") #ValueError
        elif opcion==2:
            x="10"+ 5 #TypeError
        elif opcion==3:
            diccionario = {"a":1,"b":2}
            x=diccionario["C"] #KeyError
        else:
            return "Opción no válida"
    except ValueError:
        return "Error: No se puede convertir la cadena a un número entero"
    except TypeError:
        return "Error: Tipo de dato inapropiado"
    except KeyError:
        return "Error: Clave no encontrado en el diccionario"

#Llamada a la función y muestra el mensaje de error
mensaje = manejar_errores()
print("Este es el mensaje ==> ", mensaje)
#============================================================================
"""
#Ejemplo 6
#Catch all Exceptions: Para calcular cualquier excepción
try:
    #Código que puede lanzar una excepción
    resultado = ("10"+5)
except:
    print("Se ha producido un error")


#==============================================================================
#Ejemplo 7
#Else block: Se ejecuta si no se lanza ninguna excepción en el blque try.
try:
    resultado = 10/0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(f"El resultado es {resultado}")
finally: #Este siempre va a aparecer en pantalla, mucho ojo ahí
    print("Fin de la operación")
"""
"""
#=============================================================================
#Ejemplo 8
#Manejo de divisiones por cero
def dividir(numerador,denominador):
    try:
        resultado = numerador / denominador
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    else:
        return f"El resultado es {resultado}"
    finally:
        print("Operación de división completada")
#Uso de la función
print(dividir(10,2))
print(dividir(10,0))"""









