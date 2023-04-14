

def esHeterograma(frase):
    leidas = [];
    for caracter in frase.lower():
        if caracter != " " and caracter not in leidas:
            leidas.append(caracter)
        elif caracter in leidas:
            return False
    return True

frase = input("Ingrese: ")
if esHeterograma(frase):
    print("Es heterograma")
else:
    print("No es heterograma")



