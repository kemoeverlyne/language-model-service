from fastapi import FastAPI, Depends, HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from routers import summarize, complete

app = FastAPI()

# Secret key for JWT
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Include routers from different services
app.include_router(summarize.router)
app.include_router(complete.router)

@app.get("/")
def read_root():
    return {"message": "API Gateway"}
