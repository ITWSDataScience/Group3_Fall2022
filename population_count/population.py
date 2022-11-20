import math
from PIL import Image

# population map max is 1710353
# scale other pixels accordingly

img = Image.new('RGBA', [8640, 4320], (0, 0, 0, 0))
pixel_map = img.load()

def population(pixel_map):
    with open('./gpw_pop.asc', 'r') as f:
        for i in range(6):
            f.readline() # skip pre data

        for rn in range(4320):
            k = f.readline().split(' ')
            for c in range(8640):
                cell_val = float(k[c]) # read population in grid

                if cell_val < 0: # skip pixel if no population
                    continue

                pix_val = int(math.sqrt(cell_val) * 0.5)

                pixel_map[c, rn] = (0, pix_val, 0, 100)
                # set pixel at current location to minimum gray + green based on population level
                # square root population to fit within spectrum

population(pixel_map)
img.save('population.png')

