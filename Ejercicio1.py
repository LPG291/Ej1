lista=[1,2,3,4,5]
lista.append(6)
lista.pop(1)
print("la lista: ")
for indice, producto in enumerate(lista):
    print(f"{indice}: {producto}")
