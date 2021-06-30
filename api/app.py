
from fastapi import FastAPI
import requests

app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return {"hello jb": True}


# Implement a /predict endpoint
@app.get("/predict")
def predict():
    url = 'http://localhost:8000/predict'
    params = {"artist": "John Hartford",
              "name": "Back in the Goodle Days",
              "popularity": 22}
    
    response = requests.get(url, params=params)
    response.json()
    
    return response.json()