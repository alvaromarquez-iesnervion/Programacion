from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/alumnos",
    tags=["alumnos"]
)

class Alumno(BaseModel):
    id:int
    nombre:str
    apellidos:str
    fecha_nacimiento:str
    curso:str
    repetidor: bool
    id_colegio:int


alumnos_list=[
    Alumno(id="1", nombre= "Alvaro", apellidos="Marquez", fecha_nacimiento="25-02-2002", curso="1BACH", repetidor=False, id_colegio=1)
]

@router.get("/")
def alumnos():
    return alumnos_list if alumnos_list else {"mensaje": "No hay alumnos"}
    
@router.post("/", status_code=201, response_model=Alumno)
def create_alumno(alumno:Alumno):
    alumno.id=next_id()
    alumnos_list.append(alumno)
    return alumno

@router.put("/{id}", response_model=Alumno)
def update_alumno(id:int, alumno:Alumno):
    for index, saved_alumno in enumerate(alumnos_list): 
        if saved_alumno.id == id: 
            alumno.id = id  
            alumnos_list[index] = alumno 
            return alumno 
        
    raise HTTPException(status_code=404, detail="Alumno not found") 

@router.delete("/{id}")
def delete_alumno(id:int):
    for alumno in alumnos_list:
        if alumno.id == id:
            alumnos_list.remove(alumno)
            return {}
    raise HTTPException(status_code=404, detail="alumno not found")

def next_id():
    return max((a.id for a in alumnos_list), default=0) + 1