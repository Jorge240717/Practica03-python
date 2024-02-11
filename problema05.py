class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", ", ".join(map(str, self.notas)))
        else:
            print("Notas: No asignadas")
    def set_age(self, edad):
        self.edad = edad
    def set_notas(self, *notas):
        self.notas = list(notas)
if __name__ == '__main__':
    nombre = input("Ingrese el nombre del alumno: ")
    numero_registro = input("Ingrese el número de registro del alumno: ")
    alumno = Alumno(nombre, numero_registro)
    alumno.display()    
    edad = input("Ingrese la edad del alumno: ")
    alumno.set_age(edad)
    cantidad_notas = int(input("¿Cuántas notas desea asignar al alumno?: "))
    notas = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(cantidad_notas)]
    alumno.set_notas(*notas)    
    alumno.display()