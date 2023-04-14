frase = input("Ingrese una cadena: ")
palabra = input("Ingrese una palabra: ")

palabras = frase.lower().split()

cant = palabras.count(palabra.lower())
print(cant)
