from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Feedback(BaseModel):
    ingredients: Union[str, None] = None
    time: int = 0

@app.get("/")
def read_root():
    return {"Welcome to predictions system"}

@app.get("/prediction/")
def read_item(ing: Union[str, None]):
    return {"time": random.randint(5,50)}

@app.post("/feedback/")
async def create_feedback(feedback: Feedback = None):
    return feedback
