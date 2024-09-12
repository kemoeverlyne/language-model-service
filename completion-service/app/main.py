from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Initialize the text generation pipeline
text_generator = pipeline("text-generation", model="gpt2")

@app.post("/complete")
async def complete_text(text: str):
    # Simulate a text completion task
    completion = text_generator(text, max_length=50, num_return_sequences=1)[0]["generated_text"]
    return {"completion": completion}
