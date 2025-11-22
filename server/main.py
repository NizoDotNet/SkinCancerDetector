from fastapi import FastAPI
from fastapi import  UploadFile
from keras.models import load_model
from predict import predict
model = load_model('skin-can.keras')
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
excepted_content_types = ('image/jpeg', 'image/png', 'image/jpg')
@app.post('/skin-can/detector')
def skin_can_detect(img: UploadFile):
    if(img.content_type not in excepted_content_types):
        return { 'code': 404, 'result': 'Not proper content type. Excepted .jpg, .png or .jpeg!'}
    res = predict(model, img, (200, 200))
    return { 'code': 200, 'result': res }