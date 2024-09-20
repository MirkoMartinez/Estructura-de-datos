def calcular_precio_final(costo, tipo_moneda, cantidad):
    descuentos = {
        'dolares': 0.05,
        'yenes': 0.15,
        'guaraníes': 0.20,
        'pesos': 0.10
    }
    incremento = 0.10

    if tipo_moneda in descuentos:
        descuento = descuentos[tipo_moneda]
        precio_final = costo * cantidad * (1 - descuento)
        tipo_desc = "descuento"
    else:
        descuento = incremento
        precio_final = costo * cantidad * (1 + descuento)
        tipo_desc = "incremento"

    return precio_final, tipo_desc, descuento

def emitir_recibo(nombre_comprador, nombre_empresa, tipo_moneda, tipo_desc, descuento, cantidad, costo, precio_final):
    print("\n--- Recibo ---")
    print(f"Nombre del comprador: {nombre_comprador}")
    print(f"Nombre de la empresa: {nombre_empresa}")
    print(f"Tipo de moneda: {tipo_moneda}")
    print(f"Tipo: {tipo_desc}")
    print(f"Descuento/Incremento aplicado: {descuento * 100}%")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario en pesos: {costo}")
    print(f"Precio total en pesos: {precio_final}")

def main():
    nombre_comprador = input("Ingrese el nombre del comprador: ")
    nombre_empresa = input("Ingrese el nombre de la empresa: ")
    tipo_moneda = input("Ingrese el tipo de moneda (dolares, yenes, guaraníes, pesos): ").lower()
    cantidad = int(input("Ingrese la cantidad de zapallos: "))
    costo = 1000  # Costo en pesos por zapallo

    precio_final, tipo_desc, descuento = calcular_precio_final(costo, tipo_moneda, cantidad)
    emitir_recibo(nombre_comprador, nombre_empresa, tipo_moneda, tipo_desc, descuento, cantidad, costo, precio_final)

if __name__ == "__main__":
    main()
