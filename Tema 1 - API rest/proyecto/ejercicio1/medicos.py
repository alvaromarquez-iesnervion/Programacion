from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

"""MÉDICO (Id, Nombre, Apellidos, NColegiado, Especialidad)
"""

app = FastAPI()

class Medico(BaseModel):
    id: int
    nombre: str
    apellidos: str
    ncolegiado: str
    especialidad: str

medicos_list = [
    Medico(id=1, nombre="Juan", apellidos="Pérez", ncolegiado="12345", especialidad="Cardiología"),
    Medico(id=2, nombre="Ana", apellidos="García", ncolegiado="67890", especialidad="Dermatología"),
    Medico(id=3, nombre="Luis", apellidos="Martínez", ncolegiado="54321", especialidad="Pediatría"),
    Medico(id=4, nombre="Marta", apellidos="López", ncolegiado="98765", especialidad="Neurología"),
    Medico(id=5, nombre="Carlos", apellidos="Sánchez", ncolegiado="11223", especialidad="Oncología"),
    Medico(id=6, nombre="Laura", apellidos="Fernández", ncolegiado="44556", especialidad="Ginecología"),
    Medico(id=7, nombre="Javier", apellidos="Gómez", ncolegiado="77889", especialidad="Psiquiatría"),
    Medico(id=8, nombre="Sofía", apellidos="Ruiz", ncolegiado="99001", especialidad="Endocrinología"),
    Medico(id=9, nombre="Diego", apellidos="Torres", ncolegiado="22334", especialidad="Traumatología"),
    Medico(id=10, nombre="Elena", apellidos="Ramírez", ncolegiado="55667", especialidad="Oftalmología"),
    Medico(id=11, nombre="Miguel", apellidos="Vargas", ncolegiado="88990", especialidad="Cardiología"),
]
    

@app.get("/", response_class=HTMLResponse)
def root():
    return """
        <html>
            <head>
                <title>Médicos API</title>
            </head>
            <body>
                <h1>Bienvenido a la API de Médicos </h1>
                <p><a href="/medicos">Ver lista de médicos</a></p>
            </body>
        </html>
    """


@app.get("/medicos")
def medicos():
    return medicos_list if medicos_list else {"mensaje": "No hay médicos disponibles"}

@app.get("/medicos/{medico_id}")
def medico(medico_id: int):
    medicos= [medico for medico in medicos_list if medico.id == medico_id]
    return medicos[0] if medicos else {"mensaje": "Médico no encontrado"}





    