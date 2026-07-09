
usuarios = { 101: "lol@example.com",102: "hi@example.com",103: "hello@example.com",104: "hola@example.com"
}
print("Diccionario inicial:")
print(usuarios)

correo_102 = usuarios.get(102)
print(f"\nCorreo del usuario 102: {correo_102}")

usuarios[101] = "lol_nuevo@example.com"

usuarios.pop(103)

print("\nDiccionario final en Python:")
print(usuarios)