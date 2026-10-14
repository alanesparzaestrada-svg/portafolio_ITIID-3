class BankAccount:
    """
    Representa una cuenta bancaria genérica para demostrar 
    el uso de atributos y diferentes tipos de métodos en Python.
    """
    
    # Atributo de clase: Compartido por todas las instancias de la clase.
    bank = "Banco Central"

    def __init__(self, saldo):
        """
        Constructor de la clase. 
        Se ejecuta automáticamente al crear un nuevo objeto (cuenta).
        
        Args:
            saldo (float): El monto inicial de dinero en la cuenta.
        """
        self.saldo = saldo  # Atributo de instancia (único para cada cuenta)

    def show_balance(self):
        """
        Método de instancia.
        Opera directamente con los datos del objeto actual (utiliza 'self').
        Muestra por pantalla el saldo actual de la cuenta.
        """
        print(f"El saldo del cliente es: ${self.saldo:.2f}")

    @classmethod
    def show_bank(cls):
        """
        Método de clase.
        Recibe la clase misma como primer argumento ('cls') en lugar de una instancia.
        Permite acceder o modificar atributos de la clase (como 'bank').
        """
        print(f"El nombre del banco es: {cls.bank}")

    @staticmethod
    def convert_currency(valor):
        """
        Método estático.
        Funciona como una función independiente alojada dentro de la clase.
        No recibe 'self' ni 'cls', por lo que no depende del estado de la clase ni de los objetos.
        """
        tipo_cambio = 20.0  # Tipo de cambio fijo de ejemplo
        pesos = valor * tipo_cambio
        print(f"${valor} USD equivalen a ${pesos:.2f} pesos.")


# ==========================================
# Ejemplo de uso del sistema
# ==========================================

# 1. Crear una instancia (objeto) de la clase BankAccount
cuenta1 = BankAccount(1250.00)

# 2. Llamar al método de instancia para ver el saldo del objeto creado
cuenta1.show_balance()

# 3. Llamar al método de clase directamente desde la clase (sin crear objetos)
BankAccount.show_bank()

# 4. Llamar al método estático directamente desde la clase como una utilidad
BankAccount.convert_currency(50)