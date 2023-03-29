class zapatos:

    def __init__(self, color, talla, marca):
        self.color = color
        self.talla = talla
        self.marca = marca
        self.rebaja = False
        
    def descuento(self, porcentaje):
        self.precio = self.precio - self.precio*porcentaje/100
        if porcentaje < 100:
            self.rebaja = True
    
    def infoproducto(self):
        info = f"Descripcion de los zapatos:\nmarca: {self.marca}\nprecio: {self.precio}\ntalla: {self.talla}\ncolor: {self.color}\n"
        if self.rebaja:
            info += "ESTE PRODUCTO ESTA REBAJADO"
            return info

    zapatilla = zapatos("naranja", "40", "nike")
    print(zapatilla.precio)
    zapatilla.descuento(50)
    print(zapatilla.precio)

    print(zapatilla.infoproducto())
