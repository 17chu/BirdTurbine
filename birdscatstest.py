import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time


x=pickle.load(open("xb.pickle","rb"))
y=pickle.load(open("yb.pickle","rb"))

x=x/255.0

dense_layers = [0]
layers_sizes = [64]
conv_layers = [3]

for dense_layer in dense_layers:
    for layer_size in layers_sizes:
        for conv_layer in conv_layers:
            name = "{}-conv-{}-nodes-{}-dense-{}".format(conv_layer,layer_size, dense_layer, int(time.time()))
            print(name)
            
            model =  Sequential()
            model.add(Conv2D(64,(3,3), input_shape=x.shape[1:])) #add convulution
            model.add(Activation("relu")) #activation
            model.add(MaxPooling2D(pool_size=(2,2))) #pooling
            
            for l in range(conv_layer-1):
                model.add(Conv2D(64,(3,3))) #add convulution again layer 2
                model.add(Activation("relu")) #activation
                model.add(MaxPooling2D(pool_size=(2,2))) #pooling

            model.add(Flatten())
            
            for _ in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation('relu'))

            model.add(Dense(1))
            model.add(Activation('sigmoid')) #is this really a layer?, "activation layer"
            tensorboard= TensorBoard(log_dir="logs/{}".format(name))

            model.compile(loss="binary_crossentropy",optimizer ="adam",metrics=['accuracy'])
            
            model.fit(x,y,batch_size=32,epochs = 10, validation_split=0.1, callbacks=[tensorboard]) 
#lets use a smaller batchsize our data is not in millions

model.save('64x3-CNNb.model')
