def triangulo_numeros():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def matriz5():
    for i in range(1,6):
        for j in range(1,6):
            print(end="*")
        print()

def matriz2():
    matriz = [[1,2],
              [3,4]]

    for i in matriz:
        print(i)

def matrizSuma3():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]

    suma = 0
    for i in matriz:
        suma += sum(i)
    print(suma)

def matriz3():
    matriz=[
        [1,2,3],
        [4,5,6],
        [7,8,9]]

    for i in matriz:
        print(i)

def matriz3inverso():

    matriz=[
        [1,2,3],
        [4,5,6],
        [7,8,9]]

    def invertir_matriz(matriz):
        nueva_matriz = []
        contador = 9

        for i in range(3):
            fila_invertida = []
            for j in range(3):
                fila_invertida.append(contador)
                contador -= 1
            nueva_matriz.append(fila_invertida)
        return nueva_matriz

    matriz_invertida = invertir_matriz(matriz)

    for fila in matriz_invertida:
        print(" ".join(map(str, fila)))

def promedio():

    estudiantes = 3
    asigaturas = 3

    notas = []

    for i in range(estudiantes):
        print(f"Ingrese las notas del estudiante {i+1}:")
        estudiante_notas = []

        for j in range(asigaturas):
            nota = float(input(f" Nota{j+1}: "))
            estudiante_notas.append(nota)

        notas.append(estudiante_notas)

    for i in range(estudiantes):
        promedio = sum(notas[i]) / asigaturas
        print(f"El promedio del estudiante {i+1} es: {promedio:.2f}")

def notabajalta():

    estudiantes = 2
    asignaturas = 3

    notas = []

    for i in range(estudiantes):
        print(f"Ingrese las notas del estudiante {i + 1}:")

        for j in range(asignaturas):
            nota = float(input(f"  Nota {j + 1}: "))
            notas.append(nota)

    maxima = max(notas)
    minima = min(notas)

    print(f"\nLa nota más alta es: {maxima:.2f}")
    print(f"La nota más baja es: {minima:.2f}")

def aprobado():
    estudiantes = 4
    asignaturas = 2
    aprobacion = 60

    aprobados = 0
    reprobados = 0

    for i in range(estudiantes):
        print(f"Ingrese las notas del estudiante {i + 1}:")
        suma_notas = 0

        for j in range(asignaturas):
            nota = float(input(f"  Nota {j + 1}: "))
            suma_notas += nota

        promedio = suma_notas / asignaturas

        if promedio >= aprobacion:
            aprobados += 1
        else:
            reprobados += 1

    print(f"\nEstudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {reprobados}")

def notas():
    estudiantes = 2
    asignaturas = 3

    notas = []

    for i in range(estudiantes):
        print(f"Ingrese las notas del estudiante {i + 1}:")
        estudiante_notas = []

        for j in range(asignaturas):
            nota = float(input(f"  Nota {j + 1}: "))
            estudiante_notas.append(nota)

        notas.append(estudiante_notas)

    # Mostrar todas las notas
    print("\nNotas ingresadas:")
    for i in range(estudiantes):
        print(f"Estudiante {i + 1}: {notas[i]}")

def menu():
    opciones = {
        "1": triangulo_numeros,
        "2": matriz5,
        "3": matriz2,
        "4": matrizSuma3,
        "5": matriz3,
        "6": matriz3inverso,
        "7": promedio,
        "8": notabajalta,
        "9": aprobado,
        "10": notas
    }

    while True:
        print("\n--- Menú ---")
        print("1. Triángulo de números")
        print("2. Matriz 5x5 de 5s")
        print("3. Matriz 2x2")
        print("4. Suma de matriz 3x3")
        print("5. Matriz 3x3")
        print("6. Matriz 3x3 inversa")
        print("7. Promedio de estudiantes")
        print("8. Nota más baja y alta")
        print("9. Aprobados y reprobados")
        print("10. Mostrar notas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

