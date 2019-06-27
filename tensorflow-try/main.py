import attack
from tensorflow import keras

import helper

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
start = 90
images = attack.attack(test_images[start:start + 9])[0]
for i in range(len(images)):
    print(
        helper.display_label(attack.get_label(images[i])),
        helper.display_label(attack.get_label(test_images[i + start])),
        helper.display_label(test_labels[i + start])
    )

helper.plot_images(images)
