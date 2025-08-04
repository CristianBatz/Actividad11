def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [nombre for nombre in lista[i:] if nombre < pivote]
    mayores = [nombre for nombre in lista[i:] if nombre > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores)


estudiantes = {}
opcion = 0

while opcion != 5:
    print("=== Registro Estudiantes ===")
    print("1. Registrar estudiantes")
    print("2. Mostrar todos los estudiantes y sus cursos")
    print("3. Buscar estudiante por carnet")
    print("4. registro ordenado")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue

    if opcion == 1:
        print("=== Registro ===")
        cantidad = int(input("Cantidad de estudiantes que desea registrar: "))
        while cantidad <= 0 or cantidad >= 100:
            print("Ha ingresado un numero fuera de los limites,vuelva a intentarlo")
            cantidad = int(input("Cantidad de estudiantes que desea registrar: "))

        for i in range(cantidad):
            print(f"Estudiante {i+1}")
            carnet = input("Ingrese su numero de carnet: ")
            while carnet in estudiantes:
                print("Ya hay un carnet con el mismo codigo,vuelva a intentarlo")
                carnet = input("Ingrese su numero de carnet: ")

            nombre = input("Nombre completo del estudiante: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")

            cursos = {}
            cantidadCurso = int(input("Cantidad de curso que desea registrar: "))
            while cantidadCurso <= 0 or cantidadCurso >= 50:
                print("Ha ingresado un numero fuera de los limites,vuelva a intentarlo")
                cantidadCurso = int(input("Cantidad de curso que desea registrar: "))

            for j in range(cantidadCurso):
                codigoCurso = input("Codigo del curso: ")
                while codigoCurso in cursos:
                    print("Ya se ha registrado este código de curso. Intente con otro.")
                    codigoCurso = input("Codigo del curso: ")
                nombreCursoA = input("Nombre completo del curso: ")
                tarea = float(input("Nota de la Tarea del curso (0-100) : "))
                while tarea < 0 or tarea > 100:
                    print("Nota fuera de rango")
                    tarea = float(input("Nota de la Tarea del curso (0-100) : "))
                parcial = float(input("Nota de el parcial del curso (0-100): "))
                while parcial < 0 or parcial > 100:
                    print("Nota fuera de rango")
                    parcial = float(input("Nota de el parcial del curso (0-100): "))
                proyecto = float(input("Nota de la proyecto del curso (0-100): "))
                while proyecto < 0 or proyecto > 100:
                    print("Nota fuera de rango")
                    proyecto = float(input("Nota del proyecto del curso (0-100): "))
                promedio = (tarea + parcial + proyecto) / 3
                cursos[codigoCurso] = {
                    "nombreCursoA": nombreCursoA,
                    "tarea": tarea,
                    "parcial": parcial,
                    "proyecto": proyecto,
                    "promedio": promedio
                }

            estudiantes[carnet] = {
                "nombre": nombre,
                "edad": edad,
                "carrera": carrera,
                "cursos": cursos
            }
    elif opcion == 2:
        print("=== Mostrar lista de Estudiantes y cursos ===")
        for carnet, datos in estudiantes.items():
            print(f"\nCarnet: {carnet}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("Cursos inscritos:")
            for codigo, notas in datos["cursos"].items():
                print(f"Codigo de curso: {codigo}")
                print(f"Nombre del curso: {notas['nombreCursoA']}")
                print(f"Punteo tarea: {notas['tarea']}")
                print(f"Punteo parcial: {notas['parcial']}")
                print(f"Punteo proyecto: {notas['proyecto']}")
                print(f"Promedio: {notas['promedio']:.2f}")

    elif opcion == 3:
        print("=== Buscar estudiante por carnet ===")
        buscando = input("Ingrese el numero de carnet: ")
        if buscando in estudiantes:
            estudiante = estudiantes[buscando]
            print("Estudiante encontrado")
            print(f"\nNombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Carrera: {estudiante['carrera']}")
            print("Cursos:")
            for codigo, notas in estudiante["cursos"].items():
                print(f"Codigo de curso: {codigo}")
                print(f"Nombre del curso: {notas['nombreCursoA']}")
                print(f"Punteo tarea: {notas['tarea']}")
                print(f"Punteo parcial: {notas['parcial']}")
                print(f"Punteo proyecto: {notas['proyecto']}")
                print(f"Promedio: {notas['promedio']:.2f}")
        else:
            print("Estudiante no encontrado.")

    elif opcion == 4:
        print("=== registro ordenado ===")
        print("=== Registro ordenado por nombre ===")
        lista_estudiantes = list(estudiantes.items())
        resultado = quick_sort(lista_estudiantes)
        for carnet, datos in resultado:
            print(f"\nCarnet: {carnet}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("Cursos inscritos:")
            for codigo, notas in datos["cursos"].items():
                print(f"Codigo de curso: {codigo}")
                print(f"Nombre del curso: {notas['nombreCursoA']}")
                print(f"Punteo tarea: {notas['tarea']}")
                print(f"Punteo parcial: {notas['parcial']}")
                print(f"Punteo proyecto: {notas['proyecto']}")
                print(f"Promedio: {notas['promedio']:.2f}")

    elif opcion == 5:
        print("=== Salir ===")
        print("Saliendo del programa")
        break

    else:
        print("Opción fuera de rango. Intente nuevamente.")