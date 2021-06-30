
from fastapi import FastAPI
import pandas as pd
from joblib import load

app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}


# Implement a /predict endpoint
@app.get("/predict")
def predict(acousticness,danceability,valence,duration_ms,speechiness,tempo,release_date,energy,explicit,mode,id,instrumentalness,key,liveness,loudness,artist,name):
    X_pred = {'acousticness':[float(acousticness)],
              'danceability':[float(danceability)],
              'duration_ms':int(duration_ms),
              'energy':[float(energy)],
              'explicit':int(explicit),
              'id':str(id),
              'instrumentalness':[float(instrumentalness)],
              'key':int(key),
              'liveness':float(liveness),
              'loudness':float(loudness),
              'mode':int(mode),
              'name':name,
              'release_date':release_date,
              'speechiness':float(speechiness),
              'tempo':float(tempo),
              'valence':float(valence),
              'artist':artist}
    
    X_pred_df = pd.DataFrame.from_dict(X_pred)
    model = load('model.joblib')
    popularity = int(model.predict(X_pred_df))
    
    return {'artist': artist,
            'name':name,'popularity':popularity}