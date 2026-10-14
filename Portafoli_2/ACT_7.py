    #Definición de la clase componente Motor
class Motor:
    # Método que enciende el motor
    def arrancar(self):
        print("Motor encendido")

# Definición de la clase contenedora llamada Auto
class auto:
    # Constructor que inicializa el auto creando un objeto Motor dentro de él
    def __init__(self):
        self.motor = Motor()  # Composición

    # Método del auto que utiliza el método del motor interno
    def arrancar_auto(self):
        self.motor.arrancar()  # Llama a la acción arrancar del objeto motor
        #print("motor encendido")
    

mi_auto = auto()         # Se crea la instancia del carro 
mi_auto.arrancar_auto()  # Se ordena arrancar el carro, el cual enciende su motor interno


