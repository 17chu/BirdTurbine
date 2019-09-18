import cv2
import tensorflow as tf
from pyfirmata import Arduino, util
import time

Categories = ["Bird", "Not Bird"]

def prepare(filepath):
    img_size = 75
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size,img_size))
    return new_array.reshape(-1, img_size,img_size,1)

model = tf.keras.models.load_model("64x3-CNNb.model")
#model always predicts against a list
prediction = model.predict([prepare('C:/out/bird3.jpg')])# C:/out/0.bmp or bird.jpg
print(Categories[int(prediction[0][0])])

board = Arduino("COM5")
iterator = util.Iterator(board)

if Categories[int(prediction[0][0])] == "Bird":
    iterator.start()
    count = 0
    Buzzer = board.get_pin('d:3:p')
    
    for i in range(100):
        for i in range(128):
            Buzzer.write(i)
    Buzzer.write(0)    
"""
prediction = model.predict([prepare('cat.jpg')])
print(Categories[int(prediction[0][0])])
"""
