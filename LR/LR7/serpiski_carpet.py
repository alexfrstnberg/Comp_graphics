import numpy as np
import matplotlib.pyplot as plt


def fill_square(x1, y1, size, img):
    for x in range(x1, x1+size):
        for y in range(y1, y1+size):
            img[x, y] = 0
    return img


levels = int(input("Level: "))
size = 3**levels

img = np.ones((size, size), dtype=np.uint8)

for level in range(1, levels+1):
    square_size = int(size/(3**level))
    for x in range(0, 3**level, 3):
        x = int((x+1)*square_size)
        for y in range(0, 3**level, 3):
            y = int((y+1)*square_size)
            img = fill_square(x, y, square_size, img)


plt.axis('off')
plt.imshow(img, cmap='binary')
plt.imsave('sierpinski.png', img, cmap='binary')
plt.show()
