from ast import keyword
from fastapi import FastAPI, HTTPException
from process import generate_snippet, generate_keyword

MAX_INPUT_LENGTH = 12

app = FastAPI()

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    snippet = generate_snippet(prompt)
    return {"snippet": snippet, "keyword": []}

@app.get("/generate_keyword")
async def generate_keyword_api(prompt: str):
    keyword = generate_keyword(prompt)
    return {"snippet": None, "keyword": keyword}

@app.get("/generate_snippet_and_keyword")
async def generate_keyword_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_snippet(prompt)
    keyword = generate_keyword(prompt)
    return {"snippet": snippet, "keyword": keyword}

def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input length is too long. It must be less than {MAX_INPUT_LENGTH} characters")

#uvicorn process_api:app --reload
