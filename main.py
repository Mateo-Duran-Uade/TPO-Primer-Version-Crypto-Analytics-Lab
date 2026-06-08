import funciones as f

def main(): # Autor principal: Luca Ferrari 
    """Funcion principal donde se hace la precarga de activos y se inicia el menu."""
    lst_nombre = []
    lst_ticker = []
    lst_valor = []
    lst_volumen = []
    lst_metodologia = []
    lst_unidades = []
    lst_puntaje = []

    lst_nombre.append("bitcoin")
    lst_ticker.append("BTC")
    lst_valor.append(95000.0)
    lst_volumen.append(45000000.0)
    lst_metodologia.append("HODL")
    lst_unidades.append(0.0)
    lst_puntaje.append(10)

    lst_nombre.append("ethereum")
    lst_ticker.append("ETH")
    lst_valor.append(3200.0)
    lst_volumen.append(15000000.0)
    lst_metodologia.append("Day Trading")
    lst_unidades.append(15.0)
    lst_puntaje.append(9)

    lst_nombre.append("solana")
    lst_ticker.append("SOL")
    lst_valor.append(150.0)
    lst_volumen.append(5000000.0)
    lst_metodologia.append("Swing Trading")
    lst_unidades.append(300.0)
    lst_puntaje.append(7)

    conexion = True

    while conexion:
        print("=" * 50)
        print("SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB".center(50))
        print("=" * 50)
        print("1. Registrar nuevo activo")
        print("2. Eliminar activo del sistema")
        print("3. Modificar valoración o puntaje")
        print("4. Informe general")
        print("8. Salir del programa")
        print("=" * 50)

        opcion = input("Seleccione una opción: ")
        while opcion not in ["1", "2", "3", "4", "8"]:
            print("Opción inválida.")
            opcion = input("Seleccione una opción: ")

        if opcion == "1":
            f.AltaActivo(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje)

        elif opcion == "2":
            f.BajaActivo(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje)
       
        elif opcion == "3":
            f.ModificarActivo(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje)
        
        elif opcion == "4":
            f.InformeGeneral(lst_nombre, lst_ticker, lst_valor, lst_volumen, lst_metodologia, lst_unidades, lst_puntaje)
        
        elif opcion == "8":
            conexion = f.salir(conexion)

main()