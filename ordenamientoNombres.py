def Quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [nombre for nombre in lista[1:] if nombre < pivote]
    iguales = [nombre for nombre in lista if nombre == pivote]
    mayores = [nombre for nombre in lista[1:] if nombre > pivote]

    return Quick_sort(menores) + iguales + Quick_sort(mayores)


nombres = []
opcion = 0
while opcion != 3:
    print("=== Menu ===")
    print("1 - Registrar nombres de estudiantes ")
    print("2 - Mostrar lista de estudiantes ")
    print("3 - Salir ")
    opcion = int(input("Opcion: "))

    match opcion:
        case 1:
            print("=== Registrar Estudiantes ===")
            cantidad = int(input("Cantidad de estudiantes: "))
            for i in range(cantidad):
                print(f"Estudiante #{i+1}")
                nombres.append(input("Nombre: "))

        case 2:
            print("=== Lista de Estudiantes ===")
            estudiantes = Quick_sort(nombres)
            print(f"{estudiantes}")