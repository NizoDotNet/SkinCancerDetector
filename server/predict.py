from PIL import Image
import numpy as np
import io

res = {
    0: 'benign',
    1: 'malignant'
}

def predict(model, img, target_size: tuple[int] = (200, 200)) -> str:
    img = Image.open(io.BytesIO(img.file.read()))
    img = img.resize(target_size)
    image_array = np.array(img)
    image_array = np.expand_dims(image_array, axis=0)
    res = model.predict(image_array)
    probs = model.predict(img)   
    prob = probs[0][0]                
    pred_label = int(prob >= 0.5)     
    print(res[pred_label])  
