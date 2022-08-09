'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio5.py
Autor: Programador x
Action: Convertir grados Celsius a Farenheit. 
'''
print("Convertir grados Celsius a Farenheit")
grados_celcius = float(input("Grados Celcius: "))
grados_farenheit = round(float(grados_celcius * 1.8 + 32),2)
print(grados_celcius, "grados Celcius es igual a", grados_farenheit, "grados Farenheit")