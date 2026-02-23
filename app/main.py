from fastapi import FastAPI,APIRouter
from app.db.session import engine
from app.models.user import Base 
from app.api import auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, tags=["Users"])