class Camiseta:
    def __init__(self, talla, color, precio, marca):
        self.talla = talla
        self.color = color
        self.precio = precio
        self.marca = marca

    def aplicardescuento(self, porcentaje):
        
        self.precio = self.precio - self.precio*porcentaje/100

    """ primera instancia de la clase camiseta
        """

camiseta = Camiseta("m", "negro", 100, "nike")
camisetaadidas = Camiseta("xl", "rojo", 300, "adidas")

print(camisetaadidas.precio)
camisetaadidas.aplicardescuento(50)
print(camisetaadidas.precio)
