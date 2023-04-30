def fnTotal(precio, descuento):
    return precio*descuento

r = fnTotal(100,1.15)
print(f"El precio total va a ser, {r}")

def fnRectangulo(ancho, largo):
    return ancho*largo
    
a = fnRectangulo(10,5)
print(f"El area del rectangulo es, {a}")

def fnDatos_persona(nombre, edad,ocupacion):
    print(f"La persona es {nombre},tiene {edad} años de edad, y es {ocupacion}")

fnDatos_persona("Yoshio",21,"Estudiante")