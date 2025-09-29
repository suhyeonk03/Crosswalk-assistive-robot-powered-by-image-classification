import os, sys
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import MaxPooling2D, Flatten, Conv2D, Dense
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
import numpy as np
from matplotlib import pyplot as plt
import cv2, imghdr

img = cv2.cvtColor(cv2.imread(os.path.join('n07740461_790.jpg')), cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()