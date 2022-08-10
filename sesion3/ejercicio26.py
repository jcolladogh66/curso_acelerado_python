'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion3/ejercicio26.py
Autor: ..............
Action: Muestra divisa
'''

monedas = {
  'Euro': '€',
  'Dolar': 'Us$',
  'Peso': '$'
}

continuar = True
while continuar:
    seleccion = input('Que divisa quieres (Euro, Dolar, Peso)? ')
    print(monedas[seleccion])
    continuar = input('¿Quieres otra divisa (Si/No)? ') == "Si" 