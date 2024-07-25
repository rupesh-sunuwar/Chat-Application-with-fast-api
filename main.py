from fastapi import FastAPI

import controller.chat_controller

app = FastAPI()

app.include_router(controller.chat_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
