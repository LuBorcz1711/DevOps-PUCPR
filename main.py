import random
from fastapi import FastAPI
from pydantic import BaseModal

app = FastAPI()

class Estudante(BaseModal):
    name: str
    curso: str
    ativo: bool

@app.get("/helloword")
async def root():
    return {"message": "Hello Word!"}

@app.get("/funcaoteste")
async def teste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante : Estudante):
    return estudante