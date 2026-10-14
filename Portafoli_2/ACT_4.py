# Definición de la clase padre Empleado
class Empleado:
    # Método constructor para inicializar el nombre y el salario
    def __init__(self, nombre, salario):
        self.nombre = nombre  # Guarda el nombre del empleado
        self.salario = salario  # Guarda el salario del empleado

    # Método para mostrar la información básica del empleado
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")

# Definición de la clase Gerente que hereda de Empleado
class Gerente(Empleado):
    # Constructor que recibe nombre, salario y el nuevo atributo departamento
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Reutiliza el constructor de la clase padre
        self.departamento = departamento  # Agrega el atributo exclusivo del gerente

    # Sobrescribimos el método mostrar_info para añadir más detalles
    def mostrar_info(self):
        super().mostrar_info()  # Llama al método original del padre para mostrar nombre y salario
        print(f"Departamento: {self.departamento}")  # Muestra el departamento del gerente

# --- Errores comunes en esta práctica ---
# * Olvidar llamar a 'super().__init__()' en la clase hija, lo que provoca 
#   un error porque los atributos 'nombre' y 'salario' no se inicializan.