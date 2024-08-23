class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    print("Este es el constructor de la clase padre")
              
    def Avanzar(self):
        print("Ejecutando método Avanzar de la clase padre")
    
    def Informacion(self):
        print("Marca: " , self.marca)
        print("Modelo: " , self.modelo)

