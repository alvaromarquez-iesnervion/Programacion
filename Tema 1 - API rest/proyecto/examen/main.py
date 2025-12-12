from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import alumnos, colegios
app = FastAPI()

app.include_router(alumnos.router)
app.include_router(colegios.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return {"message": "Welcome to the School API"}

