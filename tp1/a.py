# Programa para registrar inscripciones de alumnos en una universidad privada

# Título principal
print("------ Registro de Inscripción de Alumnos ------")

# Solicitar datos personales
nombre = input("Ingrese el nombre del alumno: ")
edad = int(input("Ingrese la edad del alumno: "))
fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa): ")

# Variable que muestra si posee título secundario (True/False)
posee_titulo_secundario = True  # Este dato es fijo en el programa

# Ingresar monto de matrícula
monto_matricula = float(input("Ingrese el monto de la matrícula: "))

# Calcular la cuota (monto de la matrícula + $1000)
cuota = monto_matricula + 1000

# Mostrar el valor de la cuota mensual
print(f"El valor de la cuota mensual es: ${cuota}")

# Materia con arancel especial
arancel_python = 12000
print(f"El valor del arancel especial para la materia 'Python I' es: ${arancel_python} por cuatrimestre.")

# Calcular descuento del 15% si paga en efectivo
descuento = 0.15
pago_efectivo = input("¿El alumno pagará en efectivo? (s/n): ")

if pago_efectivo.lower() == 's':
    cuota_descuento = cuota - (cuota * descuento)
    print(f"El valor de la cuota con el 15% de descuento es: ${cuota_descuento:.2f}")
else:
    cuota_descuento = cuota
    print(f"El valor de la cuota sin descuento es: ${cuota_descuento:.2f}")

# Imprimir todos los datos ingresados
print("\n------ Resumen de Inscripción ------")
print(f"Nombre del alumno: {nombre}")
print(f"Edad del alumno: {edad}")
print(f"Fecha de nacimiento del alumno: {fecha_nacimiento}")
print(f"Posee título secundario: {posee_titulo_secundario}")
print(f"Monto de matrícula: ${monto_matricula}")
print(f"Cuota mensual: ${cuota}")
print(f"Cuota con descuento (si aplica): ${cuota_descuento:.2f}")
print(f"Arancel especial 'Python I': ${arancel_python} por cuatrimestre")
