from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Word!"}

@app.get("/teste1")
async def teste():
    return {"teste": "deu certo"}