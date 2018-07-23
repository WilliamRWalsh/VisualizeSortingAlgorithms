import numpy as np
from PIL import Image
import imageio


class Visualize:
    def __init__(self, data):
        self.images = []
        self.size_mod = 20
        self.data = data
        self.num_of_points = len(data)

    def bubble_sort(self, highlight_0=-1, highlight_1=-1):
        img = Image.new("RGBA", (self.num_of_points*self.size_mod, self.num_of_points*self.size_mod), "black")
        pixels = img.load()

        for x in range(self.num_of_points * self.size_mod):
            for y in range(self.data[x//self.size_mod] * self.size_mod):
                if highlight_0 == x//self.size_mod:  # Green
                    pixels[x, y] = (0, 255, 0)
                elif highlight_1 == x//self.size_mod:  # Blue
                    pixels[x, y] = (0, 0, 255)
                else:
                    pixels[x, y] = (255, 255, 255)

        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        self.images.append(np.array(img))

    def quick_sort(self, d, i, j, red, to, fro):
        img = Image.new("RGBA", (self.num_of_points * self.size_mod, self.num_of_points * self.size_mod), "black")
        pixels = img.load()

        for x in range(self.num_of_points * self.size_mod):
            for y in range(d[x // self.size_mod] * self.size_mod):
                if i == x // self.size_mod:  # Green
                    pixels[x, y] = (0, 255, 0)
                elif j == x // self.size_mod:  # Blue
                    pixels[x, y] = (0, 0, 255)
                elif red == x // self.size_mod:  # Red
                    pixels[x, y] = (255, 0, 0)
                elif x // self.size_mod >= to and x // self.size_mod <= fro:
                    pixels[x, y] = (128, 128, 128)
                else:
                    pixels[x, y] = (255, 255, 255)

        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        self.images.append(np.array(img))

    def merge_sort(self):
        img = Image.new("RGBA", (self.num_of_points * self.size_mod, self.num_of_points * self.size_mod), "black")
        pixels = img.load()

        for x in range(self.num_of_points * self.size_mod):
            for y in range(self.data[x // self.size_mod] * self.size_mod):
                pixels[x, y] = (255, 255, 255)

        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        self.images.append(np.array(img))


    def create_gif(self, name):
        # print(self.images)
        imageio.mimsave('gifs/' + name + '.gif', self.images, duration=.2)

