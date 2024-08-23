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

class Auto(Vehiculo):
    def Arrancar(self):
        print("Método Arrancar de la clase hija Auto")

class Camion(Vehiculo):
    def Arrancar(self):
        print("Método Arrancar de la clase hija Camion")

print ("Ejercicio Herencia\n")
userSelection="1"
while userSelection!="3":

    userSelection = input("\n\nElija una opcion lo siguiente: \n1-Auto\n2-Camion\n3-Salir\n\nSu Seleccion: ")
    if(userSelection!="3"):
        userBrand = input("Ingrese la Marca del Vehiculo: ")
        userModel = input("Ingrese el Modelo del Vehiculo: ")
        if(userSelection=="1"):
            userVehicle=Auto(userBrand,userModel)
            print("\n\nTipo: Auto")
            userVehicle.Informacion()
            userVehicle.Arrancar()
            userVehicle.Avanzar()

        elif(userSelection=="2"):
            userVehicle=Camion(userBrand,userModel)
            print("\n\nTipo: Camion")
            userVehicle.Informacion()
            userVehicle.Arrancar()
            userVehicle.Avanzar()

        elif(userSelection=="3"):
            break
        
        else:
            print("Opcion Invalida:\n")
print("Saliendo...")    