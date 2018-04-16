import pickle
import numpy as np
import sys
from cArray import createArray

train_data = "C:/Users/vsrag/Documents/Projects, Papers and Presentations/SILAI/Datasets/Idols/Squared_32/train"
val_data = "C:/Users/vsrag/Documents/Projects, Papers and Presentations/SILAI/Datasets/Idols/Squared_32/validate"
test_data = "C:/Users/vsrag/Documents/Projects, Papers and Presentations/SILAI/Datasets/Idols/Squared_32/test"

# flag 0 - normal numpyness     (Any Difference?)
# flag 1 - yArray is first a list then changed to numpy


Train = createArray(train_data, 1025, 1)
Val = createArray(val_data, 225, 1)
Test = createArray(test_data, 220, 1)


# Pickling the data
print("Train shape : ", Train[0].shape, " and ", Train[1].shape)
pickle_out = open("dataset/train.p", "wb")                ################### rm 1 ###########
pickle.dump(Train, pickle_out) 

print("Val shape : ", Val[0].shape, " and ",  Val[1].shape)
pickle_out = open("dataset/validate.p", "wb")             ################### rm 1 ###########
pickle.dump(Val, pickle_out) 

print("Test shape : ", Test[0].shape, " and ", Test[0])
print("Test shape : ", Test[1].shape, " and ", Test[1])
pickle_out = open("dataset/test.p", "wb")                 ################### rm 1 ###########
pickle.dump(Test, pickle_out) 

print("It has all been pickled!")
pickle_out.close()
