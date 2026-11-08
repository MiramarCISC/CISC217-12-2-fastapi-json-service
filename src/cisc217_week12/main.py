"""FastAPI application for the Week 12 lab."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="CISC 217 Character API")

class CharacterCreate(BaseModel):
    """Request model for creating or replacing a character."""
    name: str
    health: int
    power: int

characters: dict[int, dict] = {
    1: {"id": 1, "name": "Aria", "health": 100, "power": 85},
    2: {"id": 2, "name": "Borin", "health": 120, "power": 70},
}

@app.get("/")
def root():
    return {"message": "CISC 217 Character API"}

@app.get("/characters")
def list_characters(minimum_power: int = 0, limit: int = 10):
    raise NotImplementedError

@app.get("/characters/{character_id}")
def get_character(character_id: int):
    raise NotImplementedError

@app.post("/characters", status_code=201)
def create_character(character: CharacterCreate):
    raise NotImplementedError

@app.put("/characters/{character_id}")
def replace_character(character_id: int, character: CharacterCreate):
    raise NotImplementedError

@app.delete("/characters/{character_id}")
def delete_character(character_id: int):
    raise NotImplementedError
