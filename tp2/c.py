# Función para calcular el vuelto y la cantidad de billetes de cada denominación
def calcular_vuelto(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
        return "Error: El dinero recibido es insuficiente."

    # Calcular el cambio a devolver
    vuelto = dinero_recibido - total_compra
    print(f"Vuelto total: ${vuelto}")

    # Lista con los valores de los billetes disponibles
    billetes = [500, 100, 50, 20, 10, 5, 1]
    
    # Diccionario para almacenar la cantidad de billetes de cada denominación
    cantidad_billetes = {}

    # Calcular cuántos billetes de cada denominación se necesitan
    for billete in billetes:
        cantidad = vuelto // billete  # Dividir el vuelto por el valor del billete
        vuelto %= billete  # Actualizar el vuelto con el residuo
        cantidad_billetes[billete] = cantidad

    return cantidad_billetes

# Programa principal
def main():
    try:
        # Ingresar el total de la compra y el dinero recibido
        total_compra = int(input("Ingrese el total de la compra: "))
        dinero_recibido = int(input("Ingrese el dinero recibido: "))

        # Calcular y mostrar el cambio o un mensaje de error
        resultado = calcular_vuelto(total_compra, dinero_recibido)

        if isinstance(resultado, str):
            print(resultado)  # Imprimir mensaje de error si lo hay
        else:
            # Imprimir la cantidad de billetes de cada denominación
            print("\nDesglose del vuelto:")
            for billete, cantidad in resultado.items():
                if cantidad > 0:
                    print(f"{cantidad} billete(s) de ${billete}")
    except ValueError:
        print("Por favor, ingrese valores numéricos enteros.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
