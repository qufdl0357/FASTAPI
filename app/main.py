from fastapi import FastAPI
from .routes import router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(router, prefix='/langchain')