from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/periodistas"
                   , tags=["Periodistas"])

class Periodista(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    telefono: str
    especialidad: str

periodistas_list = [
    Periodista(id=1, dni="12345678A", nombre="Carlos", apellidos="García", telefono="600123456", especialidad="Deportes"),
    Periodista(id=2, dni="23456789B", nombre="Ana", apellidos="López", telefono="600234567", especialidad="Política"),
    Periodista(id=3, dni="34567890C", nombre="Luis", apellidos="Martínez", telefono="600345678", especialidad="Cultura"),
    Periodista(id=4, dni="45678901D", nombre="Marta", apellidos="Sánchez", telefono="600456789", especialidad="Economía")]

@router.get("/")
def periodistas():
    return periodistas_list if periodistas_list else {"mensaje": "No hay periodistas disponibles"}

@router.get("/{id}")
def periodista(id:int): 
    return search_periodista(id)
@router.get("/query/") # Obtener un periodista por su ID con query parameter
def periodista(id: int):
    return search_periodista(id)

@router.post("/", status_code=201, response_model=Periodista) # Crear un nuevo periodista
def create_periodista(periodista: Periodista):
    periodista.id=next_id()  # Asignar el siguiente ID disponible
    periodistas_list.append(periodista) 
    return periodista

@router.put("/{id}", response_model=Periodista) # Actualizar un periodista existente
def update_periodista(id: int, periodista:Periodista):
    for index, saved_periodista in enumerate(periodistas_list): # Recorro la lista con índice
        if saved_periodista.id == id: # Si encuentro el periodista a actualizar
            periodista.id = id  # Le pongo el ID correcto
            periodistas_list[index] = periodista # Actualizo el periodista en la lista
            return periodista # Devuelvo el periodista actualizado
        
@router.delete("/{id}", status_code=204) # Eliminar un periodista
def delete_periodista(id: int):
    for saved_periodista in periodistas_list:
        if saved_periodista.id==id:
            periodistas_list.remove(saved_periodista)
            return {}
        raise HTTPException(status_code=404, detail="Periodista no encontrado")


def next_id():
    return max((p.id for p in periodistas_list), default=0) + 1

def search_periodista(id: int):
    periodistas=[p for p in periodistas_list if p.id == id]
    if not periodistas:
        raise HTTPException(status_code=404, detail="Periodista no encontrado")
    return periodistas[0]