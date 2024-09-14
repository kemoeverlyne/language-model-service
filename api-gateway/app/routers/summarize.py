from fastapi import APIRouter
import httpx

router = APIRouter()

@router.post("/summarize")
async def summarize(text: str, max_length: int= 100):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8001/summarize", json={"text": text, "max_length": max_length})
    return {"summary": f"Summarized version of '{text}'"}
    # Call the summarization microservice
