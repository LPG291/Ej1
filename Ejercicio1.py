lista=["uva","manzana","naranja","pera"]
lista.append("banana")
lista.pop(1)
print("la lista: ")
for indice, producto in enumerate(lista):
    print(f"{indice}: {producto}")
