import tensorflow as tf
from keras.models import load_model



model = load_model('20-11-3.keras')

while True:
    path = input()
    try:
        img = tf.keras.utils.load_img(path, target_size=(200, 200))
    except:
        continue
    img = tf.keras.utils.img_to_array(img) 
    img = tf.expand_dims(img, axis=0)  

    res = {
        0: 'benign',
        1: 'malignant'
    }

    probs = model.predict(img)   
    prob = probs[0][0]                
    pred_label = int(prob >= 0.5)     
    print(res[pred_label])  
