import operaciones
if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Ingrese números válidos.")
    else:
        print("Suma:", operaciones.suma(num1, num2))
        print("Resta:", operaciones.resta(num1, num2))
        print("Producto:", operaciones.producto(num1, num2))
        print("División:", operaciones.division(num1, num2))