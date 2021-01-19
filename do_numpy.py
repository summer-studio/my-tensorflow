import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
from matplotlib import pyplot as plt

value = tf.add(1, 2).numpy
print(value)

hello = tf.constant('Hello, TensorFlow!')
print(hello)

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()
