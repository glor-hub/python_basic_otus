from fastapi import FastAPI, Body
from schemas import UserIn, User, UserOut, UserBase
from typing import List
import crud

app = FastAPI()


@app.get("/hello/{name}")
def read_root(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/ping/", status_code=200)
def ping_view():
    return {"message": "pong"}


@app.post("/books")
def create_book(title: str = Body(...), price: int = Body(...)):
    return {"book title": title, "book price": price}

@app.post("/user")
def create_user(user_in: UserIn):
    return {"user_in": user_in.dict()}

@app.post("/users")
def create_user_for_db(user_base: UserBase):
    crud.create_user(user_base)
    return {"user": user_base.dict()}

@app.get("/users",response_model=List[UserOut])
def get_database():
    return crud.get_db()

@app.get("/users_with_id/",response_model=List[User])
def get_database():
    return crud.get_db()
