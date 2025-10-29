from fastapi import FastAPI
from routers import periodistas, articulos
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(periodistas.router)
app.include_router(articulos.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Journalists API"}