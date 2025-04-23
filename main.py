import generators, statistical_tests

def menu():
    print("Elija un generador de números aleatorios:")
    print("1. Parte central del cuadrado")
    print("2. Método de Lehmer")
    print("3. Método congruencial mixto")
    print("4. Método congruencial multiplicativo")
    print("5. Método congruencial aditivo")
    choice = int(input("Ingrese su elección (1, 2, 3, 4, 5): "))
    return choice

def statistical_test_menu():
    print("Elija una prueba estadística:")
    print("1. Prueba de los promedios")
    print("2. Prueba de la frecuencia")
    print("3. Prueba de la serie")
    print("4. Prueba de Kolmogorov-Smirnov")
    print("5. Prueba de Corrida Arriba y Abajo de la media")
    choice = int(input("Ingrese su elección (1, 2, 3, 4, 5): "))
    return choice

def main():
    generator_choice = menu()
    n = int(input("¿Cuántos números aleatorios desea generar? "))
    
    if generator_choice == 1:
        print("Generador Parte central del cuadrado.")
        seed = int(input("Ingrese la semilla: "))
        digits = int(input("Ingrese la cantidad de dígitos: "))
        numbers = generators.parte_central_cuadrado(seed, digits, n)["resultado"]
    elif generator_choice == 2:
        print("Método de Lehmer.")
        seed = int(input("Ingrese la semilla (número de 4 dígitos): "))
        t = int(input("Ingrese el valor de t: "))
        numbers = generators.lehmer(seed, t, n)["resultado"]
    elif generator_choice == 3:
        print("Método congruencial mixto.")
        seed = int(input("Ingrese la semilla: "))
        a = int(input("Ingrese el valor de a: "))
        m = int(input("Ingrese el valor de m: "))
        c = int(input("Ingrese el valor de c: "))
        numbers = generators.congruencial_mixto(seed, a, m, c, n)["resultado"]
    elif generator_choice == 4:
        print("Método congruencial multiplicativo.")
        seed = int(input("Ingrese la semilla: "))
        a = int(input("Ingrese el valor de a: "))
        m = int(input("Ingrese el valor de m: "))
        numbers = generators.congruencial_multiplicativo(seed, a, m, n)["resultado"]
    elif generator_choice == 5:
        print("Método congruencial aditivo.")
        seed_length = int(input("Ingrese la cantidad de semillas: "))
        seed = []
        for i in range(seed_length):
            seed.append(int(input(f"Ingrese el valor de la semilla {i + 1}: ")))
        m = int(input("Ingrese el valor de m: "))
        numbers = generators.congruencial_adivito(seed, m, n)["resultado"]
    else:
        print("Elección inválida.")
        return

    print("Números generados:", numbers)

    test_choice = statistical_test_menu()
    if test_choice == 1:
        print("Prueba de los promedios seleccionada.")
        za = float(input("Ingrese el valor del estadistico za: "))
        result = statistical_tests.mean_test(numbers, za)["resultado"]
    elif test_choice == 2:
        print("Prueba de la frecuencia seleccionada.")
        subintervals = int(input("Ingrese el número de subintervalos: "))
        chi_squared_a = float(input("Ingrese el valor del estadístico chi cuadrado: "))
        result = statistical_tests.frecuency_test(numbers, subintervals, chi_squared_a)["resultado"]
    elif test_choice == 3:
        print("Prueba de la serie seleccionada.")
        sub_cells = int(input("Ingrese el número de subceldas: "))
        chi_squared_a = float(input("Ingrese el valor del estadístico chi cuadrado: "))
        result = statistical_tests.series_test(numbers, sub_cells, chi_squared_a)["resultado"]
    elif test_choice == 4:
        print("Prueba de Kolmogorov-Smirnov seleccionada.")
        dan = float(input("Ingrese el valor del estadistico dan: "))
        result = statistical_tests.ks_test(numbers, dan)["resultado"]
    elif test_choice == 5:
        print("Prueba de Corrida Arriba y Abajo de la media seleccionada.")
        chi_squared_an2 = float(input("Ingrese el valor del estadístico chi cuadrado: "))
        result = statistical_tests.mean_up_and_down_test(numbers, chi_squared_an2)["resultado"]
    else:
        print("Elección inválida.")
        return
    
    if result:
        print("No se rechazo la hipotesis de que los numeros provienen de un universo uniformemente distribuido.")
    else:
        print("Se rechaza la hipotesis de que los numeros provienen de un universo uniformemente distribuido.")

if __name__ == "__main__":
    main()
    while True:
        main()
        repeat = int(input("Ingrese 0 para salir o cualquier otro número para repetir: "))
        if repeat == 0:
            print("Saliendo de la aplicación.")
            break