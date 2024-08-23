#Write a program that asks for a sequence
#(use the raw_input function) then prints it 10 times.  Include the loop count in the output

print ("\n")
print ("Ejercicio 1 - Impresion de una Cadena 10 Veces\n")
print ("------------------------------------------------------")
userSequence= input("Ingresa la Sequencia a Imprimir: ")
print ("Loop\tSequence")
for i in range(10):
    print(i,"\t",userSequence)

