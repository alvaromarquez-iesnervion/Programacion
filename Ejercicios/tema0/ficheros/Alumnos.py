from pathlib import Path

def ListaAlumnos(ruta):
    lista=[]
    with open(ruta) as f:
        for linea in f.readlines():
            linea=linea.strip()
            partes=linea.split()
            if len(partes) == 3:            
                nombre, edad, estatura = partes
                tupla = (nombre, int(edad), float(estatura))
                lista.append(tupla)            
        return lista


def muestraAlumnos(alumnos):
    for alumno in alumnos:
        print(
            f"Nombre: {alumno[0]} \n"
        )

def mediaEdad(alumnos):
    sumaEdades=0
    for alumno in alumnos:
        sumaEdades+=alumno[1]

    mediaEdad= sumaEdades/len(alumnos)
    return mediaEdad

def mediaAltura(alumnos):
    sumaAlturas=0
    for alumno in alumnos:
        sumaAlturas+= alumno[2]

    mediaAltura= sumaAlturas/len(alumnos)
    return mediaAltura

def programaAlumnos():
    ruta = Path(__file__).parent / "Alumnos.txt"
    listaAlumnos=ListaAlumnos(ruta)

    opcion = int(input(
        "Seleccione que es lo que quieres hacer:\n"
        "1. Mostrar los nombres de los alumnos\n"
        "2. Mostrar la media de las edades\n"
        "3. Mostrar la media de las alturas\n"
        "4. Salir"
        ))

    if opcion==1:
        muestraAlumnos(listaAlumnos)
    elif opcion==2:
         print(mediaEdad(listaAlumnos))
    elif opcion==3:
         print(mediaAltura(listaAlumnos))

    

