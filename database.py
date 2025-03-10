# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Example connection string (update with your PostgreSQL credentials)
DATABASE_URL = "postgresql://todo_owner:npg_hJV7BGZ1ACvz@ep-summer-dust-a10gz0p9-pooler.ap-southeast-1.aws.neon.tech/todo?sslmode=require"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
