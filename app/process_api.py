from fastapi import FastAPI
from process import generate_snippet, generate_keyword

app = FastAPI()

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    snippet = generate_snippet(prompt)
    return {"snippet": snippet}

@app.get("/generate_keyword")
async def generate_keyword_api(prompt: str):
    keyword = generate_keyword(prompt)
    return {"keyword": keyword}


#uvicorn process_api:app --reload
