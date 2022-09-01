diccionario = {
    'Nombre': 'Daniela',
    'Apellido': 'Estrada',
    'Edad': 26,
    'Estatura': 1.65,
    'Pais de nacimiento': 'Colombia',
    'Ciudad': 'Medellin',
    'Cumpleaños': '14 de noviembre',
    'Profesion': 'Programadora',
    'Nombre de la mascota': 'Canela',   
}

print(diccionario)
print(diccionario['Nombre'])
print(diccionario.get('Edad'))

# Acceder de todos los atributos y valores del diccionarios al tiempo 
# Recorrer un diccionario

for clave,valor in diccionario.items():
    print(clave,valor)

print('********************')

diccionario['¿Ya desayunó?'] = True

print(diccionario)
