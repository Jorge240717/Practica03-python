from problema03 import Circulo
from problema04 import Rectangulo
def mostrar_menu():
    print("\nMenú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")
def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo es: {area}")
def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo es: {area}")
def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    rectangulo = Rectangulo(lado, lado)  
    area = rectangulo.calcular_area()
    print(f"El área del cuadrado es: {area}")
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
if __name__ == "__main__":
    main()