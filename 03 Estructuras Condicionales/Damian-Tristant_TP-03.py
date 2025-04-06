'''Ejercicio 1

#Solicito la edad del usuario
edad_usario = int(input("Por favor, indique su edad: "))
#Realizo la comparacion
edad_usario = "Es mayor de edad" if edad_usario > 18 else "Es menor de edad"
print(edad_usario)

'''

'''Ejercicio 2

#Solicito la nota al usuario
nota_usuario = int(input("Indique su nota para saber si esta aprobado o no:"))
#Realizo la comparacion
nota_usuario = "Aprobado" if nota_usuario >=6 else "Desaprobado"
print(nota_usuario)

'''


'''Ejercicio 3

#Solicito un numero al usuario
num_par = int(input("Ingrese el numero para saber si es par o impar:"))

num_par = "Ah ingresado un numero par" if num_par %2 == 0 else "Ah ingresado un numero impar"
print(num_par)

'''


'''Ejericio 4

#Solicito al usuario que ingrese su edad
edad_usuario = int(input("Ingrese su edad: "))

#Realizo las comparaciones
if edad_usuario > 0 and edad_usuario < 12 :
    print("Pertenece a la categoria niña/o")
elif edad_usuario >= 12 and edad_usuario < 18 :
    print("Pertenece a la categoria adolecente")
elif edad_usuario >=18 and edad_usuario < 30 :
    print("Pertecene a adulto/a joven")
elif edad_usuario >= 30:
    print("Pertenece a adulto/a")
else:
    print("No pertenece a una categoria correcta")

'''


'''Ejercicio 5

#Solicito al usuario que ingrese una contraseña
contrasenia = input("Ingrese una contraseña entre 8 y 14 caracteres por favor: ")

#Comparo la longitud e imprimo por pantalla la respuesta
contrasenia = "Ah ingresado una contraseña correcta!" if len(contrasenia) >= 8 and len(contrasenia) <= 14 else "La contraseña es incorrecta!"
print(contrasenia)

'''



'''Ejercicio 6


#importa las librerias necesarias
import random
from statistics import mode, median, mean

#Creo al lista de numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(15)]


#Calculo la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

#Comparo para saber su sesgo
if media > mediana > moda :
    sesgo = "Sesgo positivo"
elif media < mediana < moda:
    sesgo = "Sesgo negativo"
else: 
    sesgo = "No hay sesgo"

print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

print(f"Resultado: {sesgo}")

'''

'''Ejericio 7

#Solicitar una palabra al usuario
palabra = input("Ingrese una palabra: ")

#Verifico que el ultimo caracter sea una vocal
if palabra[-1] in 'aeiou':
    palabra += '!'

print(palabra)

'''

'''Ejercicio 8

#Pido y almaceno nombre y opcion
nombre = input("Indique su nombre: ")
opcion = int(input("Indique 1, 2 o 3 como opciones de impresion: "))

if opcion == 1 :
    print(nombre.upper())
elif opcion == 2 :
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("A seleccionado un opcion in correcta. Seleccione 1, 2 o 3")  

'''

'''Ejercicio 9

#Pido al usuario que ingrese el valor de magnitud
valor = float(input("Ingrese la magnitud del terremoto (1 al 7)"))

if valor < 3 and valor > 0 :
    print("Muy leve")
elif valor >=3 and valor < 4 :
    print("Leve")
elif valor >= 4 and valor < 5 :
    print("Moderado")
elif valor >= 5 and valor < 6 :
    print("Fuerte")
elif valor >= 6 and valor < 7 :
    print("Muy fuerte")
elif valor >= 7 and valor < 8 :
    print("Extremo")
else:
    print("Ah ingresado una categoria no valida")

'''

'''Ejercicio 10

#Solicito al usuario en que emisferio se encuentra
hemisferio = input("En que emisferio te encuentras? N: Norte / S: Sur: ")

#Solicito mes y dia
mes = int(input("Ingresa el numero de mes (1 - 12)"))
dia = int(input("Ingrese el dia (1 - 31)"))

#Realizo la comparacion
if hemisferio == 'n':  
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"     
elif hemisferio == 's':  
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Ingrese un Hemisferio valido (N o S)"

#Imprimo el resultado
if estacion != "Ingrese un Hemisferio valido (N o S)":
    print(f"En el hemisferio {hemisferio}, el día {dia} de mes {mes} corresponde a la estación de {estacion}.")
else:
    print("Por favor, ingresa un hemisferio válido (N para Norte, S para Sur).")

'''