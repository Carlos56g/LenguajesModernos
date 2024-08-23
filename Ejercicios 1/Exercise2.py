#Write a program that asks for a sequence
#then numbers each base, one base per line.

print ("\n")
print ("Ejercicio 2 - Impresion de cada caracter de una cadena\n")
print ("------------------------------------------------------")
userSequence= input("Ingresa la Cadena que se subdividirá: ")

print ("Index\tElement")
for i in range(len(userSequence)):
    print(i+1,"\t",userSequence[i])
