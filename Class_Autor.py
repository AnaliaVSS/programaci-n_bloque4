class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Inicializar la lista de libros

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros:", ", ".join(self.libros) if self.libros else "Ninguno")

    # Método para agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro}' agregado a {self.nombre}.")

    # Método para eliminar un libro
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro}' eliminado de {self.nombre}.")
        else:
            print(f"El libro '{libro}' no se encuentra en la lista de {self.nombre}.")

# Crear una instancia de Autor
autor1 = Autor("Mario Benedetti", "Uruguayo")

# Agregar libros
autor1.agregar_libro("La Tregua")
autor1.agregar_libro("El Amor es un Mito")

# Mostrar detalles del autor
autor1.mostrar_autor()


