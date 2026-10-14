# Definición de la clase Libro
class Libro:
    # Constructor para recibir el título y las páginas
    def __init__(self, titulo, num_paginas):
        self.titulo = titulo          # Guarda el título
        self.num_paginas = num_paginas  # Guarda el número de páginas

    # Método mágico __str__: Define cómo se convierte el objeto a texto (al usar print)
    def __str__(self):
        return f"Libro: {self.titulo}, Páginas: {self.num_paginas}"

    # Método mágico __len__: Define qué devuelve la función nativa len() para este objeto
    def __len__(self):
        return self.num_paginas  # Retorna el número de páginas como longitud del libro

# Prueba de los métodos mágicos
mi_libro = Libro("Cien Años de Soledad", 417)  # Se instancia el objeto libro

print(mi_libro)         # Al imprimir el objeto, Python ejecuta automáticamente __str__
print(len(mi_libro))    # Al usar la función len(), Python ejecuta automáticamente __len__

# --- Errores comunes en esta práctica ---
# * Olvidar usar la palabra reservada 'return' dentro de estos métodos y usar 'print' 
#   en su lugar, lo que causa un error de tipo porque Python espera recibir de vuelta 
#   un valor (un texto o un número entero).