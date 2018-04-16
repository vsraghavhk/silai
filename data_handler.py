#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pickle
import numpy as np
from cArray import createArray

# train.p = dataset with 3 channels
# train1.p = dataset with 3 channels with flag 1 in cArray

TRAIN_FILE = "train.p"                         # rm 1
VALID_FILE = "validate.p"                      # rm 1
TEST_FILE = "test.p"                           # rm 1

'''
train_data = "C:/Users/vsrag/Documents/Projects, Papers and Presentations/SILAI/Datasets/Idols/train"
val_data = "C:/Users/vsrag/Documents/Projects, Papers and Presentations/SILAI/Datasets/Idols/validate"
test_data = "C:/Users/vsrag/Documents/Projects, Papers and Presentations/SILAI/Datasets/Idols/test"
'''
def get_data(folder):
    """
        Load traffic sign data
        **input: **
            *folder: (String) Path to the dataset folder
    """
    
    # Load the dataset
    training_file = os.path.join(folder, TRAIN_FILE)
    validation_file= os.path.join(folder, VALID_FILE)
    testing_file =  os.path.join(folder, TEST_FILE)

    with open(training_file, mode='rb') as f:
        train = pickle.load(f)

    with open(validation_file, mode='rb') as f:
        valid = pickle.load(f)
    
    with open(testing_file, mode='rb') as f:
        test = pickle.load(f)

    # Retrive all datas
    x_train, y_train = train[0], train[1]
    x_valid, y_valid = valid[0], valid[1]
    x_test, y_test = test[0], test[1]
    print("X shape at data handler : ", x_test.shape)
    print("Y shape at data handler : ", y_test.shape)
    
    '''
    x_train, y_train = np.asarray(createArray(train_data))
    x_valid, y_valid = np.asarray(createArray(val_data))
    x_test, y_test = np.asarray(createArray(test_data))
    '''
    return x_train, y_train, x_valid, y_valid, x_test, y_test
