import random

print("Ejemplo 1")
x = 0
while x < 10:
    print(x)
    x += 1

print("\n ///////////////// \n") #Flush?
print("Ejemplo 2")

respuesta = ""
while respuesta != "Si":
    respuesta = input("Si o no licenciado\n")
print("Calmese licenciado!")

print("\n ///////////////// \n") #Flush?
print("Ejemplo 3")

while random.randint(0,10)!= 1:
    print("10%, de probabilidad")

print("\n ///////////////// \n") #Flush?
print("Ejemplo break")

x = 0
while True:
    x+=1
    if x == 10:
        break

print("\n ///////////////// \n") #Flush?
print("Ejemplo continue")

while True:
    x -=1
    if x == 0:
        continue

def fn():
    pass
