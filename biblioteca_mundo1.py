import json


def cargar_libros(archivo):
    try:
        file = open(archivo, 'r')
        libros = json.load(file)
        file.close()
        return libros
    except:
        return []

def guardar_libros(archivo, libros):
    file = open(archivo, 'w')
    json.dump(libros, file)
    file.close()

def agregar_libro(libros):
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")
    año = input("Año de Publicación: ")
    
    
    nuevo_libro = {
        "Titulo": titulo,
        "Autor": autor,
        "Categoria": categoria,
        "Año": año
    }
    libros.append(nuevo_libro)
    print("Libro agregado.")

def editar_libro(libros):
    titulo = input("Título del libro a editar: ")
    for libro in libros:
        if libro("Titulo") == titulo:
            libro["Titulo"] = input("Nuevo título: ")
            libro["Autor"] = input("Nuevo autor: ")
            libro["Categoria"] = input("Nueva categoría: ")
            libro["Ano"] = input("Nuevo año: ")
            print("Libro editado.")
            return
    print("Libro no encontrado.")

def eliminar_libro(libros):
    titulo = input("titulo  del libro A eliminar: ")
    for libro in libros:
        if libro["Titulo"] == titulo:
            libros.remove(libro)
            print("Libro eliminado.")
            return
    print("Libro no encontrado.")

def buscar_libro(libros):
    titulo = input("Título del libro a buscar: ")
    for libro in libros:
        if libro["Titulo"] == titulo:
            print(libro)
            return
    print("Libro no encontrado.")

def mostrar_menu():
    print("******")
    print("*  mundo libro *")
    print("******")
    print("[1] - agregar libro")
    print("[2] - editar libro")
    print("[3] - eliminar libro")
    print("[4] - buscar libro")
    print("[5] - salir")


archivo_libro = ("libros.json")


libros = cargar_libros(archivo_libros)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        agregar_libro(libros)
        guardar_libros(archivo_libros, libros)
    elif opcion == '2':
        editar_libro(libros)
        guardar_libros(archivo_libros, libros)
    elif opcion == '3':
        eliminar_libro(libros)
        guardar_libros(archivo_libros, libros)
    elif opcion == '4':
        buscar_libro(libros)
    elif opcion == '5':
        break
    else:
        print("Opción no válida.")