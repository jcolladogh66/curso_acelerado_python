'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion3/ejercicio21.py
Autor: ..............
Action: Listado de asignaturas
'''

ganadores = []
otro = 1
while otro == 1:
    numero = int(input("Número ganador: "))
    ganadores.append(numero)
    otro = int(input("Desea agregar otro número (0-no, 1-si): "))

print("Números ganadores ordenados")
ganadores.sort()
for i in ganadores:
  print(i)