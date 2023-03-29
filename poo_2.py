class toys:
    def __init__(self, precio, diseño, color):
        self.precio = precio
        self.diseño = diseño
        self.color = color
    
    toysboy = toys(200, "gato", "cafe")
    print (toysboy.diseño)
    
    toysgirl = toys(150, "vaca", "azul")
    print(toysgirl.diseño)
