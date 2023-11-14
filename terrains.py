import math
import numpy as np
from PIL import Image as im

MAX_16UINT = 65535


class Terrains(object):

    def __init__(self, ter_str, sea_level):
        self.sea_level = sea_level
        ter_points_strs = ter_str.split(',')
        ter_size = int(math.sqrt(len(ter_points_strs)))
        print("Loading terrain data:", ter_size, "x", ter_size, "points")
        self.ter_points = []
        self.ter_heights = []
        self.ter_depths = []
        for ter_points_str in ter_points_strs:
            ptr_str_pair = ter_points_str.split(':')
            cur_height = int(ptr_str_pair[0])
            cur_depth = int(ptr_str_pair[1])
            self.ter_heights.append(cur_height)
            self.ter_depths.append(cur_depth)

        self.generate_heightmaps()
        self.generate_depthmaps()

    def generate_heightmaps(self):
        # Assuming self.ter_depths is a 1D array representing your custom scale
        arrayter = np.array(self.ter_heights)
        self.ter_heights = arrayter.astype(int)

        # Determine the size of the square image based on the length of self.ter_depths
        img_size = int(math.sqrt(len(self.ter_heights)))

        # Reshape the 1D array to a 2D grid
        ter_depths_grid = self.ter_heights.reshape((img_size, img_size))

        # Map the custom scale to the 0-65535 range (16-bit)


        # Convert to uint16 to fit the 16-bit range
        mapped_data = ter_depths_grid.astype(np.uint16)
        mapped_data = np.flipud(mapped_data)
        # Create an image from the mapped data
        heightmap_image = im.fromarray(mapped_data, 'I;16')  # 'I;16' mode for 16-bit unsigned integers

        # Save the image as a 16-bit TIFF file
        heightmap_image.save(f'output_heightmap_16bit_sealvl-{self.sea_level}.tiff', format='TIFF')
        heightmap_image.save(f'output_heightmap_16bit_sealvl-{self.sea_level}.png', format='png')
        print("Saved heightmaps!")

    def generate_depthmaps(self):
        # Assuming self.ter_depths is a 1D array representing your custom scale
        arrayter = np.array(self.ter_depths)
        self.ter_depths = arrayter.astype(int)

        # Determine the size of the square image based on the length of self.ter_depths
        img_size = int(math.sqrt(len(self.ter_depths)))

        # Reshape the 1D array to a 2D grid
        ter_depths_grid = self.ter_depths.reshape((img_size, img_size))

        # Map the custom scale to the 0-65535 range (16-bit)

        # Convert to uint16 to fit the 16-bit range
        mapped_data = ter_depths_grid.astype(np.uint16)
        mapped_data = np.flipud(mapped_data)
        # Create an image from the mapped data
        heightmap_image = im.fromarray(mapped_data, 'I;16')  # 'I;16' mode for 16-bit unsigned integers

        # Save the image as a 16-bit TIFF file
        heightmap_image.save(f'output_depthmap_16bit_sealvl-{self.sea_level}.tiff', format='TIFF')
        heightmap_image.save(f'output_depthmap_16bit_sealvl-{self.sea_level}.png', format='png')
        print("Saved depthmaps!")
