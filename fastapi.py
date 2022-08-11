from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Feedback(BaseModel):
    ingredients: Union[str, None] = None
    time: int = 0

class Ingredient(BaseModel):
    name: str
    unit: str
    amount: float

class PredictionRequest(BaseModel):
    recipe_text: str
    ingredients: List[Ingredient]

@router.post("/prediction/")
async def predict_cooking_time(prediction_request: PredictionRequest):
    return {
         "cooking_time": random.randint(5,50),
         "resting_time": random.randint(5,50),
         "preparation_time": random.randint(5,50)
    }


@app.get("/")
def read_root():
    return {"Welcome to predictions system"}

@app.get("/prediction_lite/")
def read_item(ing: Union[str, None]):
    return {"time": random.randint(5,50)}

# @app.post("/prediction/")
# def read_item(ing: Union[str, None]):
#     return {
#         "cooking_time": random.randint(5,50),
#         "resting_time": random.randint(5,50),
#         "preparation_time": random.randint(5,50)
#     }

@app.post("/feedback/")
async def create_feedback(feedback: Feedback = None):
    return feedback


@app.get("/prediction/")
async def predict_cooking_time(prediction_request: PredictionRequest):
    return {
        "cooking_time": 15,
        "resting_time": 2,
        "preparation_time": 5
    }
