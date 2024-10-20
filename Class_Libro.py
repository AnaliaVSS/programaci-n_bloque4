class libros: 
    def __init__(self, título ="", editorial ="", autor = ""):
        self.título = título
        self.editorial = editorial
        self.autor = autor
        self.libros = []  # Inicializar la lista de libros

    # Método para mostrar los (detalles del libro
    def mostrar_libros(self): 
            print(f"título: {self.título}") 
            print(f"editorial: {self.editorial}") 
            print(f"autor:  {self.autor}") 
            print("Libros:", ", ".join(self.libros) if self.libros else "Ninguno") 