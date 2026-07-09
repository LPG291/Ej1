
from collections import deque

cola = deque(["Ticket 1", "Ticket 2", "Ticket 3", "Ticket 4", "Ticket 5"])
print(f"Cola inicial: {list(cola)}")

atendido1 = cola.popleft()
print(f"Atendido: {atendido1}")

atendido2 = cola.popleft()
print(f"Atendido: {atendido2}")

cola.append("Ticket 6")
print("Se agrego un ticket.")

print("\n--- Entregable: Orden final de la cola ---")
print(list(cola))