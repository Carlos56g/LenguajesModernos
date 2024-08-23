#Create a new program that enter a sequence in a List 
#Enter a sequence: AGAATTC
#Insert 5 new Elements and the end
#Inverse the list CTTAAGA
#Print the total of elements
#Print the each element including
#the index

print ("\n")
print ("Ejercicio 5 - Manejo de Listas\n")
print ("------------------------------------------------------")
List=[]
ListR=[]
userSequence= input("Ingresa la Sequencia que se va a trabajar: ")

for i in range(len(userSequence)):
    List.append(userSequence[i])

print("\nTotal de Elementos: ",len(List))
print("Lista Original:\n",List)
ListR=List.copy()
print("\nLista Invertida:\n",ListR)
ListR.reverse()

print ("\nIndex\tElement")
for i in range(len(List)):
    print(i,"\t",List[i])
