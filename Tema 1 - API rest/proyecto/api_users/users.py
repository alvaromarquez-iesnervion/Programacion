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

@app.get("/users")
def users():
    return users_list

@app.get("/users/{id}")

def user(id: int):
    return search_user(id)

@app.get("/users/")
def user(id: int):
    return search_user(id)

def search_user(id: int):
    users = [user for user in users_list if user.id == id]
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    
    return users[0]