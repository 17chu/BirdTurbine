import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time
#"""

name="Cat-vs-dog-cnn-64x2-{}".format(int(time.time()))
tboard = TensorBoard(log_dir='logs/{}'.format(name))

x=pickle.load(open("x.pickle","rb"))
y=pickle.load(open("y.pickle","rb"))

x=x/255.0

model =  Sequential()
model.add(Conv2D(64,(3,3), input_shape=x.shape[1:])) #add convulution
model.add(Activation("relu")) #activation
model.add(MaxPooling2D(pool_size=(2,2))) #pooling

model.add(Conv2D(64,(3,3))) #add convulution again layer 2
model.add(Activation("relu")) #activation
model.add(MaxPooling2D(pool_size=(2,2))) #pooling

model.add(Flatten())
model.add(Dense(64)) #add a dense layer 3
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid')) #is this really a layer?, "activation layer"

model.compile(loss="binary_crossentropy",
              optimizer ="adam",
              metrics=['accuracy'])
model.fit(x,y,batch_size=32,epochs = 10, validation_split=0.1, callbacks=[tboard]) 
#lets use a smaller batchsize our data is not in millions


