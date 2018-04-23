from model_base import ModelBase
from tkinter import messagebox
from model import ModelIdol
import numpy as np 
import imutils
import cv2
import os

def capture():
    folder = "test"
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Image Capture (Space to capture)")
    # width = 1000
    # height = 1000
    # cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    # cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    while True:
        ret, frame = cam.read()
        frame = imutils.resize(frame, width = 1000)
        cv2.imshow("Image Capture (Space to capture)", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "0.png"
            path = os.path.join(folder, img_name)
            cv2.imwrite(path, frame)
            #print("{} written!".format(img_name))
            # Make second dummy copy
            img_name = "1.png"
            path = os.path.join(folder, img_name)
            cv2.imwrite(path, frame)            
            break
    cam.release()
    cv2.destroyAllWindows()

def show(idol):
    with open("signnames.csv", "r") as f:
        signnames = f.read()
    id_to_name = { int(line.split(",")[0]):line.split(",")[1] for line in signnames.split("\n")[1:] if len(line) > 0}
    if idol in id_to_name:
        name = id_to_name[idol]
    # print("The image is : ", name)
    f.close()

    idol = "{}.txt".format(idol)
    idol = os.path.join('Database', idol)
    f = open(idol, 'r')
    file_contents = f.read()
    f.close()
    # print(file_contents)
    # TKinter Message box
    messagebox.showinfo(name, file_contents)
    result = messagebox.askquestion("Again?", "Would you like to try again?", icon='warning')
    if result == 'yes':
        return 1
    else:
        return 0

def test(ckpt):

    model = ModelIdol("Idols", output_folder=None)
    # Load the model
    model.load(ckpt)
    choice = 1
    while choice == 1:
        ############### CAPTURE ##############
        capture()
        ###############   TEST  ##############
        folder = "test"
        images = []
        labels = []
        for filename in os.listdir (folder):
            img = cv2.imread(os.path.join(folder, filename))
            img = cv2.resize(img, (32, 32))
            images.append(img)
            labels.append('-1')
        # Indian Jugaad
        images = np.array(images) 
        labels = np.array(labels)

        prediction = model.predict_image(images, labels)
        '''
        with open("signnames.csv", "r") as f:
            signnames = f.read()
        id_to_name = { int(line.split(",")[0]):line.split(",")[1] for line in signnames.split("\n")[1:] if len(line) > 0}
        if prediction[0] in id_to_name:
            string = id_to_name[prediction[0]]
        print("The image is : ", string)
        '''
        ######## SHOW #############
        choice = show(prediction[1])
    
    # return prediction

def obtain():
    ckpt = "outputs/checkpoints/c1s_9_c1n_256_c2s_6_c2n_64_c2d_0.7_c1vl_16_c1s_5_c1nf_16_c2vl_32_lr_0.0001_rs_1--Idols--1523697220.148633"
    #model = ModelIdol("Idols", output_folder=None)
    # Load the model
    #model.load(ckpt)
    # capture()
    test(ckpt)
    # show(result[1])
    # return result[1]

if __name__ == '__main__':
    obtain()