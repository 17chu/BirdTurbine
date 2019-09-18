import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

DATA = "PetImages2" #data name
CATEGORIES = ["Dog","Cat"]
"""
for category in CATEGORIES:
    path = os.path.join(DATA, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap = "gray")
        plt.show()
        break
    break
"""
img_size = 75
#new_array = cv2.resize(img_array,(img_size,img_size))
#plt.imshow(new_array, cmap = 'gray')
#plt.show()

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATA, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(img_size,img_size))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass
create_training_data()
print(len(training_data))
            
            
random.shuffle(training_data) #randomize for better machine learning

for sample in training_data[:10]:
    print(sample[1])

x=[]
y=[]

for features, labels in training_data: #turning into lists
    x.append(features)
    y.append(labels)
    
x = np.array(x).reshape(-1,img_size,img_size,1) #x cannot be a list for neural network
#1 represents color values



pickle_out = open("x500.pickle","wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y500.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()
"""    
pickle_in = open("x.pickle","rb")
x = pickle.load(pickle_in)
"""

