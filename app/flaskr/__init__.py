import os
from flask import Flask
from flask import request
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
import numpy as np
from keras.models import load_model
import io 
import base64
import tensorflow as tf
from PIL import Image
from base64 import b64decode
import PIL.ImageOps
import json

def preprocess_image(image,target_size=(26,26)):

    if image.mode != "L":
        image = image.convert("L") #Convert to grayscale
    image = PIL.ImageOps.invert(image) # Flip Black/white pixels
    image = image.resize(target_size) # Size appropriately
    arr = img_to_array(image)
    arr = np.expand_dims(arr, axis=0)
    arr /= 255.
    return arr

model = load_model("ccn4-accuracy-97.5.h5") #Load Model
model.compile(loss='categorical_crossentropy',optimizer="adam",metrics=["categorical_accuracy"])
global grpah 
graph = tf.get_default_graph() #Enable tensorflow to run properly
       
def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['POST'])
    def predict():
        if request.method == 'POST':
            data_uri = request.data
            data_uri = str(data_uri, 'utf-8') # Decode the input file
            header, encoded = data_uri.split(",",1)
            decoded = b64decode(encoded)
            image = Image.open(io.BytesIO(decoded))
            pre_processed_img = preprocess_image(image,target_size=(26,26))
            def m(x):
                # In tensorflow the options are stored as (1,10,2,3,4,5,6,7,8,9),
                # aka in lexicographic order. Hence it is necessary to remap to actual
                # values.
                if x == 0:return 1
                if x == 1:return 10
                return x
            with graph.as_default(): # Allow tensorflow to run
                op = model.predict(pre_processed_img)
                res = [m(np.argmax(op)), np.max(op)]
                res[1] = str(round(res[1]*10000)/100)
                res[0] = str(res[0])
                # print(res)
                # print(json.dumps(res))
                return json.dumps(res)
                # return json.dumps(res)
                # return json.dumps([np.argmax(op), max(op)]) #reutrn prediction
        else:
            error = 'Invalid Request'      
    return app