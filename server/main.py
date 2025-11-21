from fastapi import FastAPI
import tensorflow as tf
from keras.models import load_model

model = load_model('skin-can.keras')
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

