def unificar(nombres, notas_1, notas_2):
    dic = {}
    list_nombres = [nombre.strip().strip("'") for nombre in nombres.split(",")]
    for nombre, notas1, notas2 in zip(list_nombres, notas_1, notas_2):
        dic[nombre] = [notas1, notas2]
    return dic

def calcularPromedioAlumno(lista):
    dic_promedios = {alumno: sum(lista[alumno])/len(lista[alumno]) for alumno in lista  }
    return dic_promedios

def calcularPromedioClase(promedio_alumnos):

    promedio = sum([promedio_alumnos[llave] for llave in promedio_alumnos]) / len(promedio_alumnos)
    return promedio

def mejorPromedio(lista_alumnos_promedio):
    return max(lista_alumnos_promedio.items(), key=lambda estudiante: estudiante[1])

def menorPromedio(lista_alumnos_promedio):
    return min(lista_alumnos_promedio.items(), key=lambda estudiante: estudiante[1])


# Datos
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


print(unificar(nombres, notas_1, notas_2))
lista = unificar(nombres, notas_1, notas_2)

print(calcularPromedioAlumno(lista))
print(f"El promedio de la clase es: {calcularPromedioClase(calcularPromedioAlumno(lista))}")
print(f"El mejor promedio es de: {mejorPromedio(calcularPromedioAlumno(lista))}")
print(f"El menor promedio es de: {menorPromedio(calcularPromedioAlumno(lista))}")