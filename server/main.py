from fastapi import FastAPI
from fastapi import File, UploadFile
import tensorflow as tf
from keras.models import load_model
from predict import predict

model = load_model('skin-can.keras')
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/skin-can/detector')
def skin_can_detect(img: UploadFile):
    res = predict(model, img, (200, 200))
    return { 'result': res }