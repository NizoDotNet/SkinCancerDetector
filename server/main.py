from fastapi import FastAPI
from fastapi import  UploadFile
from keras.models import load_model
from predict import predict
TF_ENABLE_ONEDNN_OPTS=0
model = load_model('skin-can.keras')
app = FastAPI()

excepted_content_types = ('image/jpeg', 'image/png', 'image/jpg')
@app.post('/skin-can/detector')
def skin_can_detect(img: UploadFile):
    if(img.content_type not in excepted_content_types):
        return { 'code': 404, 'result': 'Not proper content type. Excepted .jpg, .png or .jpeg!'}
    res = predict(model, img, (200, 200))
    return { 'code': 200, 'result': res }