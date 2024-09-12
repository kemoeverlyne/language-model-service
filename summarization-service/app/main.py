from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

@app.post("/summarize")
async def summarize(text: str):
    # Simulate a summarization task
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    return {"summary": summary}
