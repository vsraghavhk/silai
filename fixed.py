from model_base import ModelBase
from model import ModelIdol
import numpy as np 
import cv2
import os

def get_prediction(filename):
    ckpt = "outputs/checkpoints/c1s_9_c1n_256_c2s_6_c2n_64_c2d_0.7_c1vl_16_c1s_5_c1nf_16_c2vl_32_lr_0.0001_rs_1--Idols--1523697220.148633"
    #model = ModelIdol("Idols", output_folder=None)
    # Load the model
    #model.load(ckpt)
    result = idk(ckpt, filename)
    return result

def idk(ckpt, filename):
    model = ModelIdol("Idols", output_folder=None)
    # Load the model
    model.load(ckpt)
    folder = "/home/silai/silai/images/"
    print(filename)
    imgs = []
    lbls = []
    # Indian Jugaad
    img = cv2.imread(os.path.join(folder, filename))
    img = cv2.resize(img, (32, 32))
    imgs.append(img)
    imgs.append(img)
    lbls.append('0')
    lbls.append('0')
    images = np.array(imgs) 
    labels = np.array(lbls)

    prediction = model.predict_image(images, labels)
    '''
    with open("signnames.csv", "r") as f:
        signnames = f.read()
    id_to_name = { int(line.split(",")[0]):line.split(",")[1] for line in signnames.split("\n")[1:] if len(line) > 0}
    if prediction[0] in id_to_name:
        #string = id_to_name[prediction[0]]
        path = 'home/silai/silai/Databse'
        idol = "{}.txt".format(prediction[0])
        idol = os.path.join(path, idol)
        f = open(idol, 'r')
        file_contents = f.read()
        f.close()
    # print("The image is : ", string)
    '''
    return prediction[0] # file_contents

if __name__ == '__main__':
    get_prediction('1524682327153786.jpg')
