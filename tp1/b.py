# Programa para registrar notas de dos exámenes y calcular resultados

# Título principal
print("------ Registro de Notas de Exámenes ------")

# Ingresar las notas de los dos exámenes
nota_examen1 = float(input("Ingrese la nota del primer examen: "))
nota_examen2 = float(input("Ingrese la nota del segundo examen: "))

# Calcular el promedio
promedio = (nota_examen1 + nota_examen2) / 2
print(f"\nEl promedio de las dos notas es: {promedio:.2f}")

# Determinar si el alumno aprobó el último examen (nota 2)
if nota_examen2 >= 7:
    print("El alumno aprobó el segundo examen.")
else:
    print("El alumno desaprobó el segundo examen.")

# Determinar si el alumno mejoró, mantuvo o empeoró su desempeño
if nota_examen2 > nota_examen1:
    print("Mejoró su desempeño en el segundo examen.")
elif nota_examen2 == nota_examen1:
    print("Mantuvo la misma nota en ambos exámenes.")
else:
    print("Empeoró su desempeño en el segundo examen.")

# Determinar si el alumno promocionó, debe rendir final o recursar
if promedio >= 7:
    print("El alumno promocionó la materia.")
elif promedio >= 4:
    print("El alumno debe rendir final.")
else:
    print("El alumno debe recursar la materia.")
