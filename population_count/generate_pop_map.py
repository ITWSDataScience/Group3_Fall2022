from PIL import Image
import math

img = Image.new('RGB', [8640, 4320], 0) # ascii data is 8640 by 4320
pixel_map = img.load() # load pixel map for image

# population map max is 1710353
# scale other pixels accordingly

with open('gpw_pop.asc', 'r') as f:
    for i in range(6):
        f.readline() # skip pre data

    for rn in range(4320):
        k = f.readline().split(' ')
        for c in range(8640):
            cell_val = float(k[c]) # read population in grid

            if cell_val < 0: # skip pixel if no population
                continue

            pixel_map[c, rn] = (20, int(math.sqrt(cell_val) * 0.5 + 20), 20)
            # set pixel at current location to minimum gray + green based on population level
            # square root population to fit within spectrum

img.save('pop_map.png')