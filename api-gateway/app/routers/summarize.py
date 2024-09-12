from fastapi import APIRouter

router = APIRouter()

@router.post("/summarize")
async def summarize(text: str):
    # Call the summarization microservice
    return {"summary": f"Summarized version of '{text}'"}
