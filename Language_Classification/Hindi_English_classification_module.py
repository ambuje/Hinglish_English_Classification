# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:26:17 2019

@author: ambuj
"""

# load json and create model
# Write the file name of the model
import numpy as np
import keras
import matplotlib.pyplot as plt
import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from string import ascii_lowercase
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing import sequence

od=dict((ch,idx) for idx, ch in enumerate(ascii_lowercase,1))
json_file = open('D:\\Downloads\\model_relu.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
# Write the file name of the weights
loaded_model.load_weights("D:\\Downloads\\lang_class_relu_model_weights.h5")
print("Loaded model from disk")

a=input()
a=a.lower()
b=list(a)
for i in range(0,len(b)):
    qw=od.get(b[i])
    b[i]=b[i].replace(b[i],str(qw))
for i in range(0,len(b)):
    b= list(map(int,b))
for i in range(0,len(b)):
    b= list(map(int,b))
b=[b]
bb=sequence.pad_sequences(b, maxlen=30)
bb=np.array(bb)
bb=bb.reshape(1,30,1)
prediction = loaded_model.predict(bb)
print('Prediction value:',prediction[0])
if prediction[0][0] >0.5:
    print("Hindi")
else:
    print("English")





























