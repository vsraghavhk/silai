from model_base import ModelBase
from model import ModelIdol
import numpy as np 
import cv2
import os

def obtain():
    ckpt = "outputs/checkpoints/c1s_9_c1n_256_c2s_6_c2n_64_c2d_0.7_c1vl_16_c1s_5_c1nf_16_c2vl_32_lr_0.0001_rs_1--Idols--1523697220.148633"
    result = test(ckpt)
    print(result[1])
    return result[1]

def test(ckpt):
    model = ModelIdol("Idols", output_folder=None)
    # Load the model
    model.load(ckpt)
    folder = "test"
    images = []
    labels = []
    for filename in os.listdir (folder):
        img = cv2.imread(os.path.join(folder, filename))
        #if img not in None:
        images.append(img)
        labels.append('0')
    images = np.array(images)
    labels = np.array(labels)

    prediction = model.predict_image(images, labels)
    return prediction

obtain()