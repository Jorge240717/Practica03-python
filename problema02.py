def obtener_calificaciones():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista = calificaciones_str.split(',')
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Asegúrese de ingresar solo números separados por comas")
def main():
    calificaciones = obtener_calificaciones()
    print("Las calificaciones ingresadas son:", calificaciones)
if __name__ == "__main__":
    main()