class Libro:
    def __init__(self, titulo, autor, n_ejemplares, n_prestados):
        self.titulo=titulo
        self.autor=autor
        self.n_ejemplares=n_ejemplares
        self.n_prestados=n_prestados
    
    def prestamo(self):
        if self.n_prestados < self.n_ejemplares:
            self.n_prestados += 1
            return True
        return False
    
    def devolucion(self):
        if self.n_prestados > 0:
            self.n_prestados -= 1
            return True
        return False

    def __str__(self):
        return (
            f"Libro: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Número de ejemplares: {self.n_ejemplares}\n"
            f"Número de ejemplares prestados: {self.n_prestados}"
        )

        
    
    def __eq__(self, value):
        esIgual=False
        if self.titulo == value.titulo and self.autor==value.autor:
            esIgual=True
        return esIgual

    def __lt__(self, other):
        if isinstance(other, Libro):
            return self.autor < other.autor  
        return NotImplemented