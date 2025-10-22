from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()



class User(BaseModel): 
    id: int
    name: str
    surname: str
    age: int

users_list=[User(id=1, name="John", surname="Doe", age=30),
            User(id=2, name="Jane", surname="Smith", age=25),
            User(id=3, name="Alice", surname="Johnson", age=28),
            User(id=4, name="Bob", surname="Brown", age=22),
            User(id=5, name="Charlie", surname="Davis", age=35),
            User(id=6, name="Eve", surname="Miller", age=27),
            User(id=7, name="Frank", surname="Wilson", age=40),
            User(id=8, name="Grace", surname="Moore", age=32)]

#Endpoints

@app.get("/users") # Obtener todos los usuarios
def users():
    return users_list

@app.get("/users/{id}") # Obtener un usuario por su ID
def user(id: int):
    return search_user(id)

@app.get("/users/") # Obtener un usuario por su ID con query parameter
def user(id: int):
    return search_user(id)



@app.post("/users", status_code=201, response_model=User) # Crear un nuevo usuario
def create_user(user: User):
    user.id=next_id()  # Asignar el siguiente ID disponible
    users_list.append(user) 
    return user


@app.put("/users/{id}", response_model=User) # Actualizar un usuario existente
def update_user(id: int, user:User):
    for index, saved_user in enumerate(users_list): # Recorro la lista con índice
        if saved_user.id == id: # Si encuentro el usuario a actualizar
            user.id = id  # Le pongo el ID correcto
            users_list[index] = user # Actualizo el usuario en la lista
            return user # Devuelvo el usuario actualizado
    
    raise HTTPException(status_code=404, detail="User not found") # Si no lo encuentro, lanzo excepción 404    

@app.delete("/users/{id}")
def delete_user(id:int):
    for saved_user in users_list:
        if saved_user.id ==id:
            users_list.remove(saved_user)
            return {}
    raise HTTPException(status_code=404, detail="User not found")

#Funciones auxiliares

def search_user(id: int):
    users = [user for user in users_list if user.id == id] 
    if not users: # Si la lista está vacía
        raise HTTPException(status_code=404, detail="User not found") # Lanzar excepción 404
    
    return users[0]

def next_id():
    return (max(users_list, key=id).id+1)   #Consigo el ID maximo y le sumo 1
                                            #El .id final es para acceder al atributo id del objeto User

