import h5py
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
import cv2
import time, os
from impl.mask_detection_arduino import found
from impl.utilities import update_quantity

#Loading pretrained model
model_path = os.getcwd() + '/artifacts/maskDetector.h5'
model = keras.models.load_model(model_path)

def detect(img):
    # For Understandable output
    status = ['Mask','Without Mask']
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (50, 50))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    output = model.predict(x)
    output = output[0][0]
    tag = int(output)    
        
    if(status[tag]=="Mask"):      # Here mask is found and going for further process
        st = found()
        if st:
            update_quantity(st)
        return "Good to go"
    else:
        return "Mask Not Found"