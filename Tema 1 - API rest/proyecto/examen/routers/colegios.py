from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, HTTPException
from .alumnos import alumnos_list
router= APIRouter(
    prefix="/colegios",
    tags=["colegios"]
)

class Colegio(BaseModel):
    id :int
    nombre :str
    distrito :str
    tipo :str
    direccion :str

colegios_list=[
    Colegio(id=1, nombre="IESNervion", distrito="Nervion", tipo="publico", direccion="kanfdsnovn")
]

@router.get("/", response_model=list[Colegio])
def colegios():
    return colegios_list if colegios_list else {"mensaje: no hay colegios"}

@router.get("/{id}")
def colegio(id:int):
    return search_colegio(id)

@router.post("/", status_code=201, response_model=Colegio)
def create_colegio(colegio: Colegio):
    colegio.id=next_id()  # Asignar el siguiente ID disponible
    colegios_list.append(colegio) 
    return colegio

@router.get("/{id}/alumnos")
def alumnos_colegio(id:int):
    return alumnos_en_colegio(id)

@router.delete("/{id}")
def delete_colegio(id:int):
    alumnos=alumnos_colegio(id)
    for saved_colegio in colegios_list:
        if saved_colegio.id==id:
            for alumno in alumnos_list:
                if alumno in alumnos:
                    alumnos_list.remove(alumno)           
        
            colegios_list.remove(saved_colegio)
            return{}
        
        raise HTTPException(status_code=404, detail="Colegio not found") 
 


def search_colegio(id: int):
    colegios = [colegio for colegio in colegios_list if colegio.id == id] 
    if not colegios: 
        raise HTTPException(status_code=404, detail="Doctor not found") # Lanzar excepción 404
    
    return colegios[0]


def next_id():
    return max((c.id for c in colegios_list), default=0) + 1

def alumnos_en_colegio(id:int):
    return [alumno for alumno in alumnos_list if (alumno.id_colegio==id)]

