'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion3/ejercicio19.py
Autor: ..............
Action: Detecta palíndromo
'''

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo") 