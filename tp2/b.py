# Función para verificar si una fecha es válida
def es_fecha_valida(dia, mes, anio):
    # Verificar que los valores sean positivos
    if dia <= 0 or mes <= 0 or anio <= 0:
        return False

    # Verificar que el mes sea válido (1 a 12)
    if mes > 12:
        return False

    # Determinar la cantidad de días en cada mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 días
        dias_del_mes = 31
    elif mes in [4, 6, 9, 11]:  # Meses con 30 días
        dias_del_mes = 30
    elif mes == 2:  # Febrero, verificar año bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_del_mes = 29  # Año bisiesto
        else:
            dias_del_mes = 28
    else:
        return False  # Mes inválido

    # Verificar que el día sea válido
    if dia > dias_del_mes:
        return False

    return True

# Programa principal
def main():
    try:
        # Ingresar la fecha
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))

        # Invocar la función para verificar si la fecha es válida
        if es_fecha_valida(dia, mes, anio):
            print("La fecha es válida.")
        else:
            print("La fecha no es válida.")
    except ValueError:
        print("Por favor, ingrese valores numéricos enteros.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
