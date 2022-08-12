def aplica_iva(base, iva = 21):
    return base * iva 
  
base = float(input('Introduce la base imponible de la factura: '))
iva = 15
print(aplica_iva(base, iva))

