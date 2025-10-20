from fastapi import FastAPI


"""MÉDICO (Id, Nombre, Apellidos, NColegiado, Especialidad)
"""

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World!"}