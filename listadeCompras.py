#aqui cree la lista vacia
compras = []
print("Ingresa tres elementos para añadir al carrito: ")

for elements in range(3):
    elementos = input(f"ingrese el elemento {elements+1}:  ") #aqui solicite al usuario el ingreso de elementos
    compras.append(elementos)

print(f"Su lista completa es: {compras}") #aqui muestro la lista q ingreso el usuario

compras.pop() #aqui elimine el ultimo elemento y muestro el resultado
print(f"su lista actualizada despues d eliminar el ultimo elemento es: {compras}")