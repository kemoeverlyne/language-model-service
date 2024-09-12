from fastapi import FastAPI

app = FastAPI()

@app.post("/summarize")
async def summarize(text: str):
    # Simulate a summarization task
    summary = text[:50]  # Example: only take the first 50 characters
    return {"summary": summary}
