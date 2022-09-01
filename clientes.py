opcion= 100

clientes = []


print('***Empanadas inteligentes***')
print('1. Agregar clientes: ')
print('3. Busque un cliente por cedula: ')
print('0. Salir')

while(opcion != 0):
    datos = {}
    opcion = int(input('Digite una opcion: '))
    if(opcion == 1):
        datos['nombre'] = input('Digite su nombre: ') 
        datos['cedula'] = input('Digite su cédula: ')
        clientes.append(datos)
    elif(opcion == 2): 
        print(clientes)
    elif(opcion == 3):
        cedula = input('Digite la cedula: ')
        for cliente in clientes:
            if(cedula == cliente['cedula']):
                encontrado = True
            else:
                encontrado = False
            if(encontrado):
                print(f"El usuario es {cliente['nombre']}")
            else: 
                print("Opciòn no válida")
    
    elif(opcion == 0):
        break
    else: 
        print("Digite opciòn válida")
else: 
    print('Adios')

