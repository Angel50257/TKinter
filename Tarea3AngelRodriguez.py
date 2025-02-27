#Ciclos (For y While)

#1. Escribe un programa que imprima todos los números pares del 1 al 100.
def pares():
    for i in range(1,101): 
        if i % 2 == 0:
            print(i)


#2. Escribe un programa que calcule la suma de todos los números del 1 al 100. 
def suma():
    suma = 0
    for i in range(1,101):
        suma += i
    print(suma)


#3. Escribe un programa que imprima la tabla de multiplicar de cualquier número escrito del teclado.
def tabla():
    num = int(input("Ingrese un número: "))
    for i in range(1,11):
        print(num, "x", i, "=", num*i)


#4. Escribe un programa que imprima el cuadrado de cada número del 1 al 20. 
def cuadrado():
    for i in range(1,21):
        print(f"El cuadrado de {i} es: ",pow(i,2))


#5. Escribe un programa que imprima todos los números negativos desde -10 hasta -1. 
def negativos():
    for i in range(-10,0):
        print(i)


#6. Escribe un programa que calcule el promedio de una lista de números ingresada por el usuario. 
def promedio():
    lista = []
    n = int(input("Ingrese la cantidad de números a promediar: "))
    for i in range(n):
        num = int(input("Ingrese un número: "))
        lista.append(num)
    prom = sum(lista)/n
    print("El promedio es: ", prom)


#7. Escribe un programa que busque un carácter específico en una cadena de texto y cuente cuántas veces aparece. 
def buscar():
    cadena = input("Ingrese una cadena de texto: ")
    letra = input("Ingrese una letra a buscar: ")
    cont = 0
    for i in cadena:
        if i == letra:
            cont += 1
    print(f"La letra {letra} aparece {cont} veces en la cadena de texto.")


#8. Escribe un programa que imprima todos los elementos de una lista anidada. 
def anidada():
    lista = [[1,2,3],[4,5,6],[7,8,9]]
    for i in lista:
        for j in i:
            print(j)


#9. Escribe un programa que multiplique cada elemento de una lista de números por 2 y almacene los resultados en una nueva lista. 
def multiplicar():
    lista = [1,2,3,4,5]
    print(f"Lista original: {lista}")
    lista2 = []
    for i in lista:
        lista2.append(i*2)
    print(f"Lista multiplicada por 2: {lista2}")


#10. Escribe un programa que cuente del 1 al 10 utilizando un ciclo while. 
def contar():
    i = 1
    while i <= 10:
        print(i)
        i += 1  


#11. Escribe un programa que calcule la suma de todos los números del 1 al 100 utilizando un ciclo while. 
def suma_while():
    suma = 0
    i = 1
    while i <= 100:
        suma += i
        i += 1
    print(suma)


#12. Escribe un programa que calcule el factorial de un número ingresado por el usuario utilizando un ciclo while. 

def factorial():
    num = int(input("Ingrese un número: "))
    fact = 1
    i = 1
    while i <= num:
        fact *= i
        i += 1
    print(f"El factorial de {num} es: {fact}")


#13. Escribe un programa que solicite al usuario una contraseña y continúe solicitándola hasta que el usuario ingrese la contraseña correcta.
def contraseña():
    contra = "1234"
    contra2 = input("Ingrese la contraseña: ")
    while contra2 != contra:
        contra2 = input("Contraseña incorrecta, intente de nuevo: ")
    print("Contraseña correcta.")


#14. Escribe un programa que imprima todos los números pares del 1 al 20 utilizando un ciclo while. 
def pares_while():
    i = 1
    while i <= 20:
        if i % 2 == 0:
            print(i)
        i += 1


#15. Escribe un programa que cuente del 10 al 1 utilizando un ciclo while 
def contar_while():
    i = 10
    while i >= 1:
        print(i)
        i -= 1


#16. Escribe un programa que calcule el promedio de una lista de números ingresados por el usuario hasta que el usuario ingrese 'fin'. 

def promedio_while():
    lista = []
    num = input("Ingrese un número o 'fin' para terminar: ")
    while num != 'fin':
        lista.append(int(num))
        num = input("Ingrese un número o 'fin' para terminar: ")
    prom = sum(lista)/len(lista)
    print("El promedio es: ", prom)


#17. Escribe un programa que sume los dígitos de un número entero positivo ingresado por el usuario utilizando un ciclo while.
def suma_digitos():
    num = int(input("Ingrese un número entero positivo: "))
    suma = 0
    while num > 0:
        suma += num % 10
        num = num // 10
    print("La suma de los dígitos es: ", suma)


#18. Escribe un programa que solicite calificaciones (entre 0 y 100) al usuario y calcule el promedio de las calificaciones ingresadas. El programa debe continuar solicitando calificaciones hasta que el usuario ingrese un número fuera del rango (0-100). 
def promedio_calificaciones():
    lista = []
    cal = int(input("Ingrese una calificación entre 0 y 100: "))
    while cal >= 0 and cal <= 100:
        lista.append(cal)
        cal = int(input("Ingrese una calificación entre 0 y 100: "))
    prom = sum(lista)/len(lista)
    print("El promedio de las calificaciones es: ", prom)


#19. Escribe un programa que solicite al usuario un número entero positivo y luego imprima la serie de números desde 1 hasta el número ingresado. 
def serie():
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(1,num+1):
        print(i)


#20. Escribe un programa que solicite al usuario un número positivo y luego genere una secuencia decreciente desde ese número hasta 1.
def secuencia():
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(num,0,-1):
        print(i)


def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Imprimir todos los números pares del 1 al 100")
        print("2. Calcular la suma de todos los números del 1 al 100")
        print("3. Imprimir la tabla de multiplicar de un número")
        print("4. Imprimir el cuadrado de cada número del 1 al 20")
        print("5. Imprimir todos los números negativos desde -10 hasta -1")
        print("6. Calcular el promedio de una lista de números")
        print("7. Buscar un carácter específico en una cadena de texto")
        print("8. Imprimir todos los elementos de una lista anidada")
        print("9. Multiplicar cada elemento de una lista de números por 2")
        print("10. Contar del 1 al 10 utilizando un ciclo while")
        print("11. Calcular la suma de todos los números del 1 al 100 utilizando un ciclo while")
        print("12. Calcular el factorial de un número utilizando un ciclo while")
        print("13. Solicitar una contraseña hasta que sea correcta")
        print("14. Imprimir todos los números pares del 1 al 20 utilizando un ciclo while")
        print("15. Contar del 10 al 1 utilizando un ciclo while")
        print("16. Calcular el promedio de una lista de números hasta que se ingrese 'fin'")
        print("17. Sumar los dígitos de un número entero positivo")
        print("18. Calcular el promedio de calificaciones entre 0 y 100")
        print("19. Imprimir la serie de números desde 1 hasta un número ingresado")
        print("20. Generar una secuencia decreciente desde un número hasta 1")
        print("21. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            pares()
        elif opcion == 2:
            suma()
        elif opcion == 3:
            tabla()
        elif opcion == 4:
            cuadrado()
        elif opcion == 5:
            negativos()
        elif opcion == 6:
            promedio()
        elif opcion == 7:
            buscar()
        elif opcion == 8:
            anidada()
        elif opcion == 9:
            multiplicar()
        elif opcion == 10:
            contar()
        elif opcion == 11:
            suma_while()
        elif opcion == 12:
            factorial()
        elif opcion == 13:
            contraseña()
        elif opcion == 14:
            pares_while()
        elif opcion == 15:
            contar_while()
        elif opcion == 16:
            promedio_while()
        elif opcion == 17:
            suma_digitos()
        elif opcion == 18:
            promedio_calificaciones()
        elif opcion == 19:
            serie()
        elif opcion == 20:
            secuencia()
        elif opcion == 21:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()