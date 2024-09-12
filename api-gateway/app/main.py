from fastapi import FastAPI, Depends
from routers import summarize, complete

app = FastAPI()

# Include routers from different services
app.include_router(summarize.router)
app.include_router(complete.router)

@app.get("/")
def read_root():
    return {"message": "API Gateway"}
