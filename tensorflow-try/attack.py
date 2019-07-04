import copy
from tensorflow import keras
import numpy as np
import time
import random
import ssim

model = keras.models.load_model("model.h5")


def random_attack(image, max_time=500):
    label = get_label(image)
    for loop in range(5):
        new_image = change_cross_random(image, r=loop + 1)
        i = 0
        while (get_label(new_image) == label or ssim.SSIM(new_image, image) < 0.7) and i < max_time:
            i += 1
            new_image = change_cross_random(image, r=loop + 1)
        if i < max_time:
            return new_image
    return None


def get_label(image):
    return np.argmax(model.predict(
        np.expand_dims(image, 0)
    )[0])


def change_cross_random(image, r=1):
    image = copy.deepcopy(image)
    (width, height) = image.shape
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    color = random.randint(0, 255)
    for w in range(r):
        if y + w < width:
            for i in range(height):
                image[i][y + w] = color
        if x + w < height:
            for i in range(width):
                image[x + w][i] = color
    return image


def all_zero_attack(image):
    (width, height) = image.shape
    return [[0] * width for _ in range(height)]


def attack(images, debug=True):
    start = time.time()
    succ = 0
    ssim_ave = 0
    indicates = []
    size = len(images)

    for loop in range(3):
        start = time.time()
        succ = 0
        ssim_ave = 0
        gen_images = []
        for i in range(size):
            new_image = random_attack(images[i], max_time=300)
            if (new_image is not None) and (not get_label(new_image) == get_label(images[i])):
                # 攻击成功
                succ += 1
                ssim_ave += ssim.SSIM(new_image, images[i])
                gen_images.append(new_image)
            else:
                # 失败
                gen_images.append(all_zero_attack(images[i]))
        print("cost", time.time() - start)
        print(succ, ssim_ave / size)
        indicates.append((gen_images, succ, ssim_ave / size))

    # 寻找最优解
    res_index = 0
    max_succ = 0
    max_ssim = 0
    for i in range(len(indicates)):
        (succ, ssim_ave) = indicates[i][1:]
        if succ > max_succ:
            res_index = i
            max_succ = succ
            max_ssim = ssim_ave
        elif succ == max_succ and ssim_ave > max_ssim:
            res_index = i
            max_ssim = ssim_ave

    res = indicates[res_index]
    print(res[1:])
    return res
