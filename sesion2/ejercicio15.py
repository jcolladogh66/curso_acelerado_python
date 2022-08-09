'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: ..............
Action: suma valores ingresados por teclado
'''
suma = 0
for i in range(10):
    valor = int(input("Ingrese valor:"))
    suma = suma + valor
print("La suma es")
print(suma)
promedio = suma / 10
print("El promedio es:")
print(promedio) 

