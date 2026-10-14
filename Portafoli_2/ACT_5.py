# Definición de la primera clase padre (Contador)
class Contador:
    # Método que simula la generación de un reporte
    def generar_reporte(self):
        print("Generando reporte financiero")

# Definición de la segunda clase padre (Técnico)
class Tecnico:
    # Método que simula la reparación de una máquina
    def reparar_maquina(self):
        print("Reparando máquina")

# Definición de la clase Jefe que hereda de ambas clases (Herencia Múltiple)
class Jefe(Contador, Tecnico):
    pass  # La palabra pass indica que no agregamos código nuevo, solo heredamos todo

# Probando la clase Jefe creando una instancia
jefe_general = Jefe()
jefe_general.generar_reporte()  # Utiliza el método heredado de la clase Contador
jefe_general.reparar_maquina()  # Utiliza el método heredado de la clase Técnico

# --- Errores comunes en esta práctica ---
# * Conflictos de nombres (problema del diamante): Si ambas clases padre tuvieran 
#   un método con el mismo nombre, Python ejecutaría el de la clase escrita primero 
#   en el paréntesis (orden MRO).