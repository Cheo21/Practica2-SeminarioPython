evaluar = """ título: Experiences in Developing a Distributed Agent-based 
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""


def analizarTexto(texto):
    oraciones = texto.split(".")
    print(oraciones)
    resultado = {"facil": 0, "aceptable": 0, "dificil": 0, "muyDificil": 0}

    for oracion in oraciones:
        palabras = oracion.split()

        if len(palabras) <= 12:
            resultado["facil"] += 1
        elif 12 < len(palabras) < 18:
            resultado["aceptable"] += 1
        elif 18 < len(palabras) < 25:
            resultado["dificil"] += 1
        elif len(palabras) > 25:
            resultado["muyDificil"] += 1
    return resultado



titulo = evaluar.split("resumen:")[0]
texto = evaluar.split("resumen:")[1]


print(analizarTexto(texto))

