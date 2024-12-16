from fastapi import FastAPI

from app.routes import items_router

app = FastAPI()

app.include_router(items_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
