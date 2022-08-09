'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: ..............
Action: imprime tabla de multiplicar
'''

n = int(input("Introduce el número (entero positivo): "))
for i in range(1,11):
    print(str(n) + " X " + str(i) + " = " + str(n * i))

