import random

Comparador = input("Siempre se debe de enviar codigo para revisar a la branch main? (True o False)\n")

print("Ejemplo 1, github curso")

if Comparador is True:
    print("No, se debe de trabajar en la branch dev")
else:
    print("Correcto, main es la branch que debe ser mas cuidada de errores")

print("\n ///////////////// \n") #Flush?
print("Ejemplo 2, tirada de dado dnd")

d20 = random.randint(1,20)
if d20 <= 19:
    print(d20)
else:
    print("CRITICO")

print("\n ///////////////// \n") #Flush?
print("Ejemplo 3, Comparador par e impar")

verificador = int(input("Ingrese cualquier numero\n"))
if verificador%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")



