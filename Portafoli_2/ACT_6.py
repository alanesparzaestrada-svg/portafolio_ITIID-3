# Función externa que recibe cualquier objeto trabajador
def calcular_pago(trabajador):
    trabajador.pago()  # Llama al método 'pago' del objeto recibido, sin importar su clase específica

# Primera clase con su propia implementación del método pago
class EmpleadoTiempoCompleto:
    def pago(self):
        print("Pago mensual fijo calculado")

# Segunda clase con otra implementación distinta del método pago
class EmpleadoPorHoras:
    def pago(self):
        print("Pago por horas trabajadas calculado")

# Pruebas del polimorfismo
fijo = EmpleadoTiempoCompleto()     # Creamos un objeto de tiempo completo
por_horas = EmpleadoPorHoras()     # Creamos un objeto por horas

calcular_pago(fijo)      # La función procesa el objeto y ejecuta su pago correspondiente
calcular_pago(por_horas) # La misma función procesa el otro objeto con su propia lógica

# --- Errores comunes en esta práctica ---
# * Pasar a la función un objeto que no tenga definido el método 'pago()', 
#   lo cual genera un error de tipo (AttributeError).