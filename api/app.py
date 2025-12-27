from fastapi import FastAPI
from pydantic import BaseModel
from core.summarizer import summarize_url

app = FastAPI()

class Request(BaseModel):
    url: str

@app.post("/summarize")
def summarize(req: Request):
    return {"summary": summarize_url(req.url)}

