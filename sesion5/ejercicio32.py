

def elimina(listin, usuario):
    del listin[usuario]
    return listin[usuario]

# Principal
listin = {'Juan':123456789, 'Pedro':987654321}
print(elimina(listin, 'Pablo')) 