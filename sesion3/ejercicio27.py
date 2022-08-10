'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion3/ejercicio27.py
Autor: ..............
Action: Muestra datos personales
'''

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su teléfono: ")

datos = {
  'nombre': nombre,
  'edad' : edad,
  'direccion': direccion,
  'telefono': telefono
}

print(datos['nombre'] + ' tiene ' + str(datos['edad']) + ' años, vive en ' + datos['direccion'] + ' y su número de teléfono es ' + datos['telefono'])