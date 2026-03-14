from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello Word!"}

@app.get("/funcaoteste")
async def teste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}