from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

@app.get("/")
def home():
    return{"message":"Backend Running"}

@app.post("/notes")
def create_note(note : Note):
    return{
        "title":note.title,
        "content":note.content

    }