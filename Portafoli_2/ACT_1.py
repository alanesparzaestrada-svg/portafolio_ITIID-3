class Car:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def show_info(self):
        print(f"Auto - Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")

# Creación de dos objetos de la clase Car
auto1 = Car("Toyota", "Corolla", "Rojo")
auto2 = Car("Ford", "Mustang", "Negro")

# Llamada al método para mostrar su información
auto1.show_info()
auto2.show_info()