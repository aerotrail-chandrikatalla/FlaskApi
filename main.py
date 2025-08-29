from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    subject: str
    description: str

@app.post("/notes/", status_code=status.HTTP_201_CREATED)
def create_note(note: Note):
   
    return {
        "message": "Note created successfully",
        "note": note
    }
