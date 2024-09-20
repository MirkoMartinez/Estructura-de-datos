# Programa que organiza las aulas, carga y valida edades, calcula promedios y costos del comedor

# a. Listado de aulas según el número de día
print("------ Listado de Aulas ------")
print("Día\tAula")
for dia in range(1, 7):  # Días del 1 al 6
    if dia % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"
    print(f"{dia}\t{aula}")

# b. Carga de edades con validación de mayores de 18
print("\n------ Carga de Edades ------")
cargas_erroneas = 0
while True:
    try:
        edad = int(input("Ingrese la edad del alumno (ingrese 0 para salir): "))
        if edad == 0:
            break
        elif edad >= 18:
            print(f"Edad ingresada correctamente: {edad}")
        else:
            print("Error: El alumno debe ser mayor de edad.")
            cargas_erroneas += 1
    except ValueError:
        print("Error: Ingrese un número válido.")
        cargas_erroneas += 1

print(f"Cantidad de cargas erróneas realizadas: {cargas_erroneas}")

# c. Cálculo del promedio de notas de 5 alumnos
print("\n------ Promedio de Notas ------")
suma_notas = 0
for i in range(1, 6):  # Alumnos del 1 al 5
    while True:
        try:
            nota = float(input(f"Ingrese la nota del alumno {i}: "))
            if 0 <= nota <= 10:  # Validación de que la nota esté en el rango válido
                suma_notas += nota
                break
            else:
                print("Error: Ingrese una nota válida entre 0 y 10.")
        except ValueError:
            print("Error: Ingrese un número válido.")

promedio = suma_notas / 5
print(f"El promedio de las notas es: {promedio:.2f}")

# d. Cálculo del costo del comedor por días
print("\n------ Costo del Comedor ------")
costo_por_dia = 1250
print("Días\tCosto Total")
for dias in range(1, 7):  # Días del 1 al 6
    costo_total = dias * costo_por_dia
    print(f"{dias}\t${costo_total}")
