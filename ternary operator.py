print("Ejemplo 1")

calificacion = input("Ingrese su calificacion semestral mas reciente\n")

becas_procentaje = 80 if float(calificacion) >= 75.0 else 40
print(f"El porcentaje de beca que se puede ofrecer es de: {becas_procentaje}%")

print("\n ///////////////// \n") #Flush?
print("Ejemplo 2")

beca_disponible = True
costo_colegiatura = 7000
descuento = 1+(becas_procentaje/100)
becas_total = costo_colegiatura*descuento if bool(beca_disponible) == True else costo_colegiatura

print("\n ///////////////// \n") #Flush?
print("Ejemplo 3")

x = 5
y = 10
result = "X es mayor" if x > y else "Y es mayor" if y > x else "X & Y son iguales"
print(result)