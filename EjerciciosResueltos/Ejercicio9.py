
def valor(palabra):
    total = 0
    valor = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    for letra in palabra.upper():
        for llave in valor:
            if letra in valor[llave]:
                total += llave

    return total


palabra = input("Ingrese una palabra: ")
print(f"El valor de la palabra: {palabra} es {valor(palabra)}")
