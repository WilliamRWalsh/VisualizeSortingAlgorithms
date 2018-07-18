import numpy as np
from PIL import Image
import imageio


class Visualize:
    def __init__(self, num_of_points, dd):
        self.num_of_points = num_of_points
        self.images = []
        self.size_mod = 20
        self.data = list(dd)

    def bubble_sort(self, d, i, j, red, to, fro):
        img = Image.new("RGBA", (self.num_of_points*self.size_mod, self.num_of_points*self.size_mod), "black")
        pixels = img.load()

        for x in range(self.num_of_points * self.size_mod):
            for y in range(d[x//self.size_mod] * self.size_mod):
                if i == x//self.size_mod:  # Green
                    pixels[x, y] = (0, 255, 0)
                elif j == x//self.size_mod:  # Blue
                    pixels[x, y] = (0, 0, 255)
                elif red == x//self.size_mod:  # Red
                    pixels[x, y] = (255, 0, 0)
                elif x//self.size_mod >= to and x//self.size_mod <= fro:
                    pixels[x, y] = (128, 128, 128)
                else:
                    pixels[x, y] = (255, 255, 255)

        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        self.images.append(np.array(img))

    def merge_sort(self, l0, l1, r0, r1, k):
        img = Image.new("RGBA", (self.num_of_points * self.size_mod, self.num_of_points * self.size_mod), "black")
        pixels = img.load()

        for x in range(self.num_of_points * self.size_mod):
            for y in range(self.data[x // self.size_mod] * self.size_mod):
                if l0 == x // self.size_mod:  # Green
                    pixels[x, y] = (0, 255, 0)
                elif r0 == x // self.size_mod:  # Blue
                    pixels[x, y] = (0, 0, 255)
                else:
                    pixels[x, y] = (255, 255, 255)

        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        self.images.append(np.array(img))

        # make the swap here
        if l0 == -1 or r0 == -1:
            return

        if self.data[l0] > self.data[r0]:
            temp_arr = self.data[l0:r0]
            self.data[k] = self.data[r0]
            while temp_arr:
                k += 1
                self.data[k] = temp_arr.pop(0)

    def create_gif(self, name):
        # print(self.images)
        imageio.mimsave(name + '.gif', self.images, duration=.2)

