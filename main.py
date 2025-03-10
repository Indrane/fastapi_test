# main.py
from fastapi import FastAPI
from routes import auth, todo
from models.base import Base
from database import engine

app = FastAPI()

app.include_router(auth.router)
app.include_router(todo.router)

@app.on_event("startup")
def startup():
    # Create database tables if they do not exist
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")


