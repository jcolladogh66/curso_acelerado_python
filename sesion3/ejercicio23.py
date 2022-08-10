'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion3/ejercicio23.py
Autor: ..............
Action: muestra producto escalar
'''

a = (1, 2, 3)
b = (-1, 0, 2)
c = (3, 2, 4)

product = 0
for i in range(len(a)):
    product += a[i]*b[i]*c[i]
  
print("El producto escalar de los vectores" + str(a) + ", " + str(b) + " y " + str(c) + " es " + str(product))  
