class Libro:
    def __init__(self, titulo, autor, n_ejemplares, n_prestados):
        self.titulo=titulo
        self.autor=autor
        self.n_ejemplares=n_ejemplares
        self.n_prestados=n_prestados
    
    def prestamo(self):
        if self.n_ejemplares>self.n_prestados:
            self.n_prestados+=1
            print("Se ha prestado el libro correctamente")
        else:
            print("No quedan ejemplares de ese libro disponibles para prestar")

    def devolucion(self):
        if self.n_prestados!= 0:
            self.n_prestados+=1
            print("Se ha devuelto el libro correctamente")
        else:
            print("no se ha prestado ningun ejemplar de ese libro")

    def __str__(self):
        cadena= "Libro: " + self.titulo + "\n"
        cadena+= "Autor " + self.autor + "\n"
        cadena += "Numero de ejemplares " + self.n_ejemplares + "\n"
        cadena += "Numero de libros prestados " + self.n_prestados + "\n"

        return cadena
    
    def __eq__(self, value):
        esIgual=False
        if self.titulo == value.titulo and self.autor==value.autor:
            esIgual=True
        return esIgual

    def __lt__(self, value):
        esMenor=False
        if self.titulo < value.titulo:
            esMenor=True
        return esMenor