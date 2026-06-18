import random

def AltaActivo(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje): # Autor principal: Mateo Duran
    """Registra activos cripto en el sistema."""

    metodologias = ["Scalping", "Day Trading", "Swing Trading", "HODL"]

    nombreactivo = str(input("Ingrese el nombre del activo (fin para finalizar): "))
    while nombreactivo.lower() != "fin":
        lst_nombre_lower = []
        for n in lst_nombre:
            lst_nombre_lower.append(n.lower())
        if nombreactivo == "":
            print("El nombre no puede quedar vacío.")

        elif nombreactivo.lower() in lst_nombre_lower:
            print("Activo existente, por favor reingréselo.")

        else:
            ticker = input("Ingrese el ticker (3 a 5 letras): ").upper()
            while not 3 <= len(ticker) <= 5 or ticker in lst_ticker:
                if not 3 <= len(ticker) <= 5:
                    print("Ticker inválido.")
                else:
                    print("Ticker existente, por favor reingréselo.")
                ticker = input("Ingrese el ticker (3 a 5 letras): ").upper()

            valor = round(random.uniform(100, 100000), 2)
            volumen = round(random.uniform(0, 50000000), 2) 
            metodologia = random.choice(metodologias)
            unidades = round(random.uniform(0, 500), 2)
            puntaje = random.randint(1, 10)

            lst_nombre.append(nombreactivo)
            lst_ticker.append(ticker)
            lst_valor.append(valor)
            lst_volumen.append(volumen)
            lst_metodologia.append(metodologia)
            lst_unidades.append(unidades)
            lst_puntaje.append(puntaje)

            print("Activo registrado correctamente.")

        nombreactivo = input("Ingrese el nombre del activo (fin para finalizar): ")

def BajaActivo(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje): # Autor principal: Mateo Duran
    """Elimina un activo cripto del sistema, buscándolo por su ticker."""

    ticker = str(input("Ingrese el ticker del activo: "))

    while ticker.upper() not in lst_ticker:
        print("Ticker invalido.")
        ticker = str(input("Ingrese el ticker del activo: "))

    indice = 0
    while lst_ticker[indice] != ticker.upper(): 
        indice += 1

    if lst_unidades[indice] != 0:
        print("No se puede eliminar el activo, debe tener 0 unidades en tesorería.")

    else:
        confirmacion = str(input(f"Activo a eliminar: {lst_nombre[indice].title()}, ¿Desea confirmar? (Si para confirmar): "))

        if confirmacion.lower() == "si":
            lst_nombre.pop(indice)
            lst_ticker.pop(indice)
            lst_valor.pop(indice)
            lst_volumen.pop(indice)
            lst_metodologia.pop(indice)
            lst_unidades.pop(indice)
            lst_puntaje.pop(indice)
            print("¡Activo eliminado correctamente!")

        else:
            print("Operación cancelada.")

def ModificarActivo(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje): # Autor principal: Luca Ferrari
    """Modifica un valor específico del activo deseado buscandolo mediante nombre."""

    
    nombre = str(input("Ingrese el nombre del activo a modificar: "))
    lst_nombre_lower = []
    for n in lst_nombre:
        lst_nombre_lower.append(n.lower())
    while nombre.lower() not in lst_nombre_lower:
        print("Nombre inválido, reingréselo.")
        nombre = str(input("Ingrese el nombre del activo a modificar: "))

    indice = 0
    while lst_nombre[indice].lower() != nombre.lower(): 
        indice += 1
    if len(lst_nombre) == 0:
        print("Sistema sin elementos a modificar")
    else:
        print("¿Qué desea modificar?")
        print("1. Valor de referencia")
        print("2. Volumen")
        print("3. Metodología")
        print("4. Unidades")
        print("5. Puntaje")
        print("6. Nombre")
        print("7. Ticker")

    opcion = input("Seleccione una opcion: ")
    while opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Opción inválida.")
        opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nuevo_valor = input("Nuevo valor (USD): ")
        while not nuevo_valor.isdigit() or int(nuevo_valor) <= 0:
            if not nuevo_valor.isdigit():
                print("Ingrese un valor numérico válido.")
            else:
                print("El valor debe ser mayor a 0.")
            nuevo_valor = input("Nuevo valor (USD): ")
        lst_valor[indice] = float(nuevo_valor)
        print("Valor actualizado correctamente.")

    elif opcion == "2":
        nuevo_volumen = input("Nuevo volumen 24hs (USD): ")
        while not nuevo_volumen.isdigit():
            print("Ingrese un valor numérico válido.")
            nuevo_volumen = input("Nuevo volumen 24hs (USD): ")
        lst_volumen[indice] = float(nuevo_volumen)
        print("Volumen actualizado correctamente.")

    elif opcion == "3":
        metodologias = ["Scalping", "Day Trading", "Swing Trading", "HODL"]
        print("Metodologías: Scalping / Day Trading / Swing Trading / HODL")
        nueva_metodologia = str(input("Nueva metodología: "))
        while nueva_metodologia not in metodologias:
            print("Metodología invalida.")
            nueva_metodologia = str(input("Nueva metodología: "))
        lst_metodologia[indice] = nueva_metodologia
        print("Metodología actualizada correctamente.")

    elif opcion == "4":
        nuevas_unidades = input("Nuevas unidades en tesorería: ")
        while not nuevas_unidades.isdigit(): #revisar porque puede haber unidades con coma
            print("Ingrese un valor numérico válido.")
            nuevas_unidades = input("Nuevas unidades en tesorería: ")
        lst_unidades[indice] = float(nuevas_unidades)
        print("Unidades actualizadas correctamente.")

    elif opcion == "5":
        nuevo_puntaje = input("Nuevo puntaje (1 al 10): ")
        while not nuevo_puntaje.isdigit() or not (1 <= int(nuevo_puntaje) <= 10):
            if not nuevo_puntaje.isdigit():
                print("Ingrese un número entero válido.")
            else:
                print("El puntaje debe estar entre 1 y 10.")
            nuevo_puntaje = input("Nuevo puntaje (1 al 10): ")
        lst_puntaje[indice] = int(nuevo_puntaje)
        print("Puntaje actualizado correctamente.")

    elif opcion == "6":
        lst_nombre_lower = []
        for nombre in lst_nombre:
            lst_nombre_lower.append(nombre.lower())
        nuevo_nombre = input("Nuevo nombre del activo: ")
        while nuevo_nombre == "" or nuevo_nombre.lower() in lst_nombre_lower:
            if nuevo_nombre == "":
                print("El nombre no puede quedar vacío.")
            else:
                print("Ese nombre ya existe, reingréselo.")
            nuevo_nombre = input("Nuevo nombre del activo: ")
        lst_nombre[indice] = nuevo_nombre
        print("Nombre actualizado correctamente.")

    elif opcion == "7":
        nuevo_ticker = input("Nuevo ticker (3 a 5 letras): ").upper()
        while not 3 <= len(nuevo_ticker) <= 5 or nuevo_ticker in lst_ticker:
            if not 3 <= len(nuevo_ticker) <= 5:
                print("Ticker inválido.")
            else:
                print("Ticker existente, por favor reingréselo.")
            nuevo_ticker = input("Nuevo ticker (3 a 5 letras): ").upper()
        lst_ticker[indice] = nuevo_ticker
        print("Ticker actualizado correctamente.")

def InformeGeneral(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje): # Autor principal: Mateo Duran
    """Ordena y muestra todos los activos del sistema en base a su puntaje de mayor a menor, con su nombre respectivo."""

    listas = [lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje]
    filas = len(lst_nombre)
    columnas = len(listas)

    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(listas[c][f])

    for recorrido in range(1, len(matriz)):
        for i in range(len(matriz) - recorrido):
            if matriz[i][6] < matriz[i+1][6] or (matriz[i][6] == matriz[i+1][6] and matriz[i][0] > matriz[i+1][0]): 
                aux = matriz[i]
                matriz[i] = matriz[i+1]
                matriz[i+1] = aux
    if len(matriz) != 0:

        print("=" * 60)
        print("INFORME GENERAL - ACTIVOS")
        print("=" * 60)
        print("")
        encabezado = ["Nombre", "Ticker", "Valor USD", "Volumen", "Metodologia", "Unidades", "Puntaje"]
        for titulo in encabezado:
            print("%-15s" % titulo, end="")
        print()
        print("-" * 105)

        for f in range(len(matriz)):
            for c in range(len(matriz[f])):
                print("%-15s" % str(matriz[f][c]).title(), end="")
            print()
    else: 
        print("Informe invalido, Sistema sin elementos")

def salir(conexion): # Autor principal: Luca Ferrari
    """Baja la bandera de conexión, terminando el bucle del menú."""

    print("\n¡Hasta luego! Cerrando el sistema...")
    conexion = False
    return conexion
