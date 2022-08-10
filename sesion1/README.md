# Sesion 1

---
Listado de ejercicios

* ejercicio1.py

Descripción: Solicitar variables


```python

'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion/ejercicio1.py
Autor: Programador x
Action: asignación de variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = ['Chiapas','Campeche',' Veracruz']
productos_produce = ['Cacao',  'Coco', 'Caña']
print(nombre_estado, "es un estado que ", )
print("colinda al sur", "con", estados_cercanos[0], "y")
print("Tiene una superficie de ", superficie) 
print("Población total: ", poblacion_total)
print("Promedio de temperatura: ", promedio_temperatura)
print("Productos que produce: ", productos_produce[0], ',', productos_produce[1], 'y', productos_produce[2] )
```

* ejercicio2.py

Descripcion: superficie de un cuadrado

```python
'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion/ejercicio2.py
Autor: Programador x
Action: superficie de un cuadrado
''' 
lado=input("Ingrese la medida del lado del cuadrado:")
lado=float(lado)
superficie=lado*lado
print("La superficie del cuadrado es")
print(superficie) 
```

* ejercicio3.py

Descripcion: pago de trabajador
```python

'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Programador x
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
horas_extras = float(input("Introduce las horas extras: "))
paga = (horas + horas_extras) * coste
print("Tu paga es", paga) 

```
