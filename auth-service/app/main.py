from fastapi import FastAPI, HTTPException

app = FastAPI()

users_db = {
    "user@example.com": {
        "username": "user",
        "password": "secret",
    }
}

@app.post("/login")
async def login(username: str, password: str):
    user = users_db.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": "fake-jwt-token"}
