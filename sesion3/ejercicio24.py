'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion3/ejercicio24.py
Autor: ..............
Action: datos personales
'''

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si" 