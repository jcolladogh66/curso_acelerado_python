'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio4.py
Autor: Programador x
Action: indice de masa corporal peso en kg/ estatura mtrs cuadrados
'''
peso = input("¿Cuál es tu peso en kg?: ")
estatura = input("¿Cuál es tu estatura en metros?: ")
imc = round(float(peso)/float(estatura)**2, 2)
print("Tu índice de masa corporal es ", str(imc))