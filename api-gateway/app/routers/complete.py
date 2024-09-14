from fastapi import APIRouter
import httpx

router = APIRouter()

@router.post("/complete")
async def complete_text(prompt: str, max_length: int = 100):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8002/completion", json={"prompt": prompt, "max_length": max_length})
        return {"complete Text": f"Complete version of '{prompt}'"}
