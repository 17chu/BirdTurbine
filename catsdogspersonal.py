import cv2
import tensorflow as tf

Categories = ["Dog", "Cat"]

def prepare(filepath):
    img_size = 75
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size,img_size))
    return new_array.reshape(-1, img_size,img_size,1)

model = tf.keras.models.load_model("64x3-CNN500.model")
#model always predicts against a list
prediction = model.predict([prepare('wolf.jpg')])
print(Categories[int(prediction[0][0])])

prediction = model.predict([prepare('dog.jpg')])
print(Categories[int(prediction[0][0])])