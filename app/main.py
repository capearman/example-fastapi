from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from . import models
from .database import engine
from .routers import post, user, auth, vote
from.config import settings

#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#models.Base.metadata.create_all(bind=engine) #don't need this after installing alembic. Creates tables when app starts up

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my api!"}





