from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/articulos"
                   , tags=["Artículos"])

class Articulo(BaseModel):
    id: int
    titulo:str
    cuerpo:str
    fecha: str
    id_periodista: int

articulos_list = [
    Articulo(id=1, titulo="Título 1", cuerpo="Cuerpo del artículo 1", fecha="2024-01-01", id_periodista=1),
    Articulo(id=2, titulo="Título 2", cuerpo="Cuerpo del artículo 2", fecha="2024-01-02", id_periodista=2),
    Articulo(id=3, titulo="Título 3", cuerpo="Cuerpo del artículo 3", fecha="2024-01-03", id_periodista=1)]

@router.get("/")
def articulos():
    return articulos_list if articulos_list else {"mensaje": "No hay articulos disponibles"}

@router.get("/{id}")
def articulos(id:int):
    return search_articulo(id)

@router.get("/query/")
def articulo(id:int):
    return search_articulo(id)

@router.post("/", status_code=201, response_model=Articulo)
def create_articulo(articulo: Articulo):
    articulo.id=next_id()
    articulos_list.append(articulo)
    return articulo

router.put("/{id}", response_model=Articulo)
def update_articulo(id:int, articulo: Articulo):
    for index, saved_articulo in enumerate(articulos_list):
        if saved_articulo.id==id:
            articulo.id=id
            articulos_list[index]=articulo
            return articulo
        
@router.delete("/{id}", status_code=204)
def delete_articulo(id:int):
    for saved_articulo in articulos_list:
        if saved_articulo.id==id:
            articulos_list.remove(saved_articulo)
            return {}
    raise HTTPException(status_code=404, detail="Articulo no encontrado")



def search_articulo(id:int):
    articulos=[articulo for articulo in articulos_list if articulo.id==id]
    if not articulos:
        raise HTTPException(status_code=404, detail="Aritculo no encontrado")
    return articulos[0]

def next_id():
    return max((a.id for a in articulos_list), default=0)+1