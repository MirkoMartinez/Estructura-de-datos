# Función para encontrar el mayor estricto de tres números
def mayor_estricto(a, b, c):
    if a > b:
        if a > c:
            if b != a and c != a:
                return a
    if b > a:
        if b > c:
            if a != b and c != b:
                return b
    if c > a:
        if c > b:
            if a != c and b != c:
                return c
    return None  # No hay mayor estricto

# Programa principal
def main():
    # Ingresar los tres números
    try:
        num1 = float(input("Ingrese el primer número positivo: "))
        num2 = float(input("Ingrese el segundo número positivo: "))
        num3 = float(input("Ingrese el tercer número positivo: "))
        
        # Verificar que los números sean positivos
        if num1 <= 0 or num2 <= 0 or num3 <= 0:
            print("Todos los números deben ser positivos.")
            return
        
        # Invocar la función para encontrar el mayor estricto
        resultado = mayor_estricto(num1, num2, num3)
        
        # Mostrar el resultado
        if resultado is not None:
            print(f"El mayor número estricto es: {resultado}")
        else:
            print("No existe un mayor estricto.")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
