# routes/todo.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.todo import TodoCreate, TodoUpdate, TodoOut
from models.todo import Todo
from models.user import User
from database import get_db
from utils.auth import get_current_user

router = APIRouter(prefix="/api/todos", tags=["todos"])

@router.post("/", response_model=TodoOut)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=False,
        user_id=current_user.id
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/", response_model=list[TodoOut])
def get_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role == "admin":
        todos = db.query(Todo).all()
    else:
        todos = db.query(Todo).filter(Todo.user_id == current_user.id).all()
    return todos

@router.put("/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if current_user.role != "admin" and db_todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if current_user.role != "admin" and db_todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    db.delete(db_todo)
    db.commit()
    return {"detail": "Todo deleted"}
