"""
#1. Escribe un programa que pida al usuario dos números y luego imprima la suma de esos números. 

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

suma=num1+num2

print(f"La suma de {num1} y {num2} es: {suma}")

#2. Escribe un programa que pida al usuario un número entero y determine si es par o impar.

num=int(input("Ingresa un numero entero: "))

if num%2==0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")

#3. Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

celsius=float(input("Ingresa un la temperatura en Celsius: "))

# Convertir a grados Fahrenheit 
fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura de {celsius} C* son {fahrenheit} *F")

#4. Escribe un programa que pida al usuario tres números y determine cuál de ellos es el mayor.

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))
num3=int(input("Ingresa el tercer numero: "))

# Determinar el número mayor 
mayor = max(num1, num2, num3) 

print(f"El numero mayor es {mayor}")

#5. Escribe un programa que pida al usuario un número entero y calcule su factorial. 

num=int(input("Ingresa un numero entero: "))

#Calcular el factorial
factorial=1

for i in range(1,num+1):
    factorial*=i
    
print(f"El factorial de {num} es: {factorial}")

#6. Escribe un programa que pida al usuario una cadena y la imprima al revés.

cadena=(input("Ingresa una cadena: "))

# Invertir la cadena 
cadena_invertida=cadena[::-1]

print(f"La dadena invertida es: {cadena_invertida}")

#7. Escribe un programa que pida al usuario una cadena y cuente cuántas vocales contiene.

cadena=(input("Ingresa una cadena: "))
vocales=("aeiouAEIOU")
#Contar las vocales
contador=sum(1 for letra in cadena if letra in vocales)
print(f"Esta cadena tiene {contador} vocales")

#8. Escribe un programa que pida al usuario una lista de números separados por comas y calcule la media de esos números.

numeros=[int(i) for i in input("Ingrese una lista de números separados por comas: ").split(",")]

# Calcular la media 
media = sum(numeros) / len(numeros)

print(f"La media de estos numeros es {media}")

#9. Escribe un programa que pida al usuario una cadena y determine si es un palíndromo (una palabra que se lee igual de izquierda a derecha que de derecha a izquierda). 

cadena=input("Ingresa una cadena: ")

# Verificar si es un palíndromo 
if  cadena == cadena[::-1]:
    print("Es un palindromo")
else:
    print("No es un palindromo")    

#10. Escribe un programa que imprima la tabla de multiplicar de un número ingresado por el usuario.

numero=int(input("Ingrese el numero que desea obtener la tabla de multiplicar: "))

# Imprimir la tabla de multiplicar 
print(f"Tabla de multiplicar del {numero}:") 
for i in range(1, 11): 
    print(f"{numero} x {i} = {numero * i}")

#11. Escribe un programa que convierta una distancia dada en kilómetros a millas. (1 kilómetro = 0.621371 millas) 

kilometros=float(input("Ingrese los kilómetros: "))

# Convertir a millas 
millas = kilometros * 0.621371 
milla=round(millas,2)#round para redondear el float

print(f"{kilometros}km son: {milla}mi")

#12. Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero. 

num=int(input("Ingresa un número: "))

if num>0:
    print("El número es POSITIVO")
elif num<0:
    print("El número es NEGATIVO")    
else:
    print("EL numero es CERO")    

#13. Escribe un programa que pida al usuario una cadena y cuente cuántas palabras contiene. 

cadena=input("Ingresa una cadena: ")

# Contar las palabras 
palabras = cadena.split() 
numero_palabras = len(palabras) 

print(f"Esta cadena tiene {numero_palabras} palabras")

#14. Escribe un programa que pida al usuario dos números: la base y el exponente, y calcule la potencia. 

base=int(input("Ingresa la base: "))
exponente=int(input("Ingresa el exponente: "))

potencia=pow(base,exponente)
# Imprimir el resultado 
print(f"{base} elevado a la potencia de {exponente} es {potencia}")

#15. Encontrar el mayor y menor en una lista 

numeros=[int(i) for i in input("Ingrese una lista de números: ").split()]

# Determinar el mayor y el menor número 
mayor = max(numeros) 
menor = min(numeros) 

print(f"El numero menor de la lista es: {menor} y el mayor es: {mayor}")
"""