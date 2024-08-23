from Auto import Auto
from Camion import Camion

def main():
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
                userVehicle.Apagar()

            elif(userSelection=="2"):
                userVehicle=Camion(userBrand,userModel)
                print("\n\nTipo: Camion")
                userVehicle.Informacion()
                userVehicle.Arrancar()
                userVehicle.Avanzar()
                userVehicle.Apagar()

            elif(userSelection=="3"):
                break
            
            else:
                print("Opcion Invalida:\n")
    print("Saliendo...")    

if __name__ == "__main__":
    main()