class Person: #definición de la clase Person
    def __init__(self, nombre, edad, ciudad):#creación de objetos de la clase Person
        self.nombre = nombre
        self.edad = edad   #definición de los atributos
        self.ciudad = ciudad

    def greet(self):# definimos el método greet que acepta el objeto self
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}.") #mostrar información

# Creación de tres objetos de la clase Person
persona1 = Person("Ana", 25, "México")
persona2 = Person("Carlos", 30, "Argentina")
persona3 = Person("Lucía", 22, "España")

# Llamada al método greet() para cada objeto
persona1.greet()
persona2.greet()
persona3.greet()