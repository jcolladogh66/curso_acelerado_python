'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion3/ejercicio27.py
Autor: ..............
Action: Gestión de facturas
'''

facturas = {}

menu = ('1. Añadir factura','2. Pagar factura', '3. Terminar')

continuar = True
while continuar:
    for i in menu:
        print(i)
    opcion = int(input("Selecciona una opción: "))
  
    if opcion == 1:
        folio = input('Introduce un número de factura: ')
        valor = float(input('Introduce el valor de la factura: '))
        facturas[folio] = valor
        print(facturas)
    elif opcion == 2:
        folio = input('Introduce un número de factura: ')
        del(facturas[folio])
        print(facturas)
    elif opcion == 3:
        print("Gracias por usar el programa")
        continuar = False
    else:
        print("Opción inválida")

