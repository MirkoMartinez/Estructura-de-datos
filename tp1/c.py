# Programa para organizar aulas, calcular descuentos y asignar estacionamiento

# Título principal
print("------ Organización de Aulas y Otros Servicios ------")

# a. Aulas: Ingresar el número de día y determinar el aula correspondiente
dia = int(input("Ingrese el número del día de la semana (1 para Lunes, 6 para Sábado): "))

if 1 <= dia <= 6:  # Verificar que el número de día sea válido
    if dia % 2 == 0:
        print("Los alumnos cursan en el aula A-300.")
    else:
        print("Los alumnos cursan en el aula A-315.")
else:
    print("Número de día inválido. Ingrese un valor entre 1 y 6.")

# b. Descuento: Calcular el descuento en la cuota
monto_cuota = float(input("Ingrese el monto de la cuota: "))
turno = input("¿El alumno cursa en el turno Tarde? (s/n): ").lower()
cantidad_materias = int(input("Ingrese el número de materias a las que se inscribe: "))

if turno == 's' and cantidad_materias > 3:
    descuento = 0.25  # 25% de descuento para alumnos del turno tarde con más de 3 materias
    print(f"El alumno tiene un descuento especial del 25%.")
else:
    descuento = 0.05  # 5% de descuento para otros casos
    print(f"El alumno tiene un descuento del 5%.")

cuota_con_descuento = monto_cuota - (monto_cuota * descuento)
print(f"El valor de la cuota con el descuento aplicado es: ${cuota_con_descuento:.2f}")

# c. Estacionamiento: Asignar costo diario según el medio de transporte
transporte = input("\n¿El alumno viene en auto, moto o bicicleta? (auto/moto/bici): ").lower()

if transporte == 'auto' or transporte == 'moto':
    costo_estacionamiento = 300  # Costo para auto o moto
elif transporte == 'bici':
    costo_estacionamiento = 50  # Costo para bicicleta
else:
    costo_estacionamiento = 0  # No se asigna costo si ingresa otro medio
    print("No se asignó costo de estacionamiento. Medio de transporte no válido.")

if costo_estacionamiento > 0:
    print(f"El costo diario de estacionamiento para {transporte} es: ${costo_estacionamiento}")
else:
    print("No se asignó ningún costo de estacionamiento.")
