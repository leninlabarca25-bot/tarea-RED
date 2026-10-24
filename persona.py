import json

# 1. Abrir y leer el archivo JSON
with open("persona.json", "r", encoding="utf-8") as archivo:
    persona = json.load(archivo)  

# 2. Mostrar los datos
print(" Informacion de Persona ")
print("Nombre:", persona["nombre"])
print("Apellido:", persona["apellido"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

# 3. El valor true del JSON se convierte en True en Python
if persona["Trabaja"]:
    print("Trabaja: Sí")
else:
    print("Trabaja: No")

# 4. Recorrer la lista de habilidades
print("\n Mis Habilidades")
for habilidad in persona["habilidades"]:
    print("-", habilidad)
input()

