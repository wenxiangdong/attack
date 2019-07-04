import attack
from tensorflow import keras

import helper

# fashion_mnist = keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# start = 90
# images = attack.attack(train_images[start:start + 9])[0]
# for i in range(len(images)):
#     print(
#         "攻击后", helper.display_label(attack.get_label(images[i])),
#         "攻击前", helper.display_label(attack.get_label(train_images[i + start])),
#         "实际", helper.display_label(train_labels[i + start])
#     )
#
# helper.plot_images(images)


def aiTest(images, shape):
    (count, w, h) = shape
    images = images.reshape((count, w, h))
    return attack.attack(images)[0]
