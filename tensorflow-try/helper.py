import copy
from matplotlib import pyplot as plt

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


def display_label(index):
    return class_names[index]


def change_pixels(xs, image):
    new_image = copy.deepcopy(image)
    xs = xs.astype(int)

    pixels = [xs[i:i + 3] for i in range(0, len(xs), 3)]
    for pixel in pixels:
        [x, y, color] = pixel
        pixel[x][y] = color
    return new_image


def plot_images(images):

    # Create a figure with sub-plots
    fig, axes = plt.subplots(3, 3, figsize=(10, 10))

    # Adjust the vertical spacing
    hspace = 0.2

    fig.subplots_adjust(hspace=hspace, wspace=0.0)

    for i, ax in enumerate(axes.flat):
        # Fix crash when less than 9 images
        if i < len(images):
            # Plot the image
            ax.imshow(images[i])

            # Show true and predicted classes
        # Remove ticks from the plot
        ax.set_xticks([])
        ax.set_yticks([])

    # Show the plot
    plt.show()
