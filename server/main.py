from fastapi import FastAPI
from fastapi import  UploadFile
from keras.models import load_model
from predict import predict
TF_ENABLE_ONEDNN_OPTS=0
model = load_model('skin-can.keras')
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/skin-can/detector')
def skin_can_detect(img: UploadFile):
    res = predict(model, img, (200, 200))
    return { 'result': res }