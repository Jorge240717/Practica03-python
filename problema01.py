def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y (X e Y son enteros, X ≤ Y, Y ≠ 0): ")
            x, y = map(int, fraccion.split('/'))
            if x <= 0 or y <= 0:
                raise ValueError("X e Y deben ser enteros positivos")
            if x > y:
                raise ValueError("X debe ser menor o igual que Y")
            return x, y
        except ValueError as ve:
            print("Error:", ve)
        except ZeroDivisionError:
            print("Error: Y no puede ser cero")
def calcular_porcentaje(x, y, total):
    porcentaje = (x / y) * 100
    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return round(porcentaje)
def main():
    while True:
        try:
            total = float(input("Ingrese el total de combustible en el tanque: "))
            if total <= 0:
                raise ValueError("El total debe ser un número positivo")
            break
        except ValueError:
            print("Error: Ingrese un número válido para el total")
    x, y = obtener_fraccion()
    while True:
        try:
            porcentaje = calcular_porcentaje(x, y, total)
            if porcentaje == 'E':
                print("La fracción es menor al 1% del total, el tanque está vacío.")
            elif porcentaje == 'F':
                print("La fracción es mayor al 99% del total, el tanque está lleno.")
            else:
                print(f"El tanque tiene aproximadamente {porcentaje}% de combustible.")
            break
        except ZeroDivisionError:
            print("Error: Y no puede ser cero")
        except ValueError:
            print("Error: La fracción ingresada no es válida")
        x, y = obtener_fraccion()
if __name__ == "__main__":
    main()