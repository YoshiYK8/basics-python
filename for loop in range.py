print("Ejemplo 1")

limite = int(input("Ingrese cantidad de segundos a contar\n"))
for cronometro in range(0, limite, 1):
    print(f"{cronometro}, segundos\n")

print("\n ///////////////// \n") #Flush?
print("Ejemplo 2")

for retrocede in range(limite, 0, -1):
    print(f"{retrocede}, segundos\n")

print("\n ///////////////// \n") #Flush?
print("Ejemplo 3")

Array = ["Hola", "como", "estas"]
for x in Array:
    print(x)