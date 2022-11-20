from PIL import Image

img = Image.new('RGBA', [8640, 4320], (0, 0, 0, 0)) # ascii data is 8640 by 4320
pixel_map = img.load() # load pixel map for image

def init_map(pixel_map):
    with open('./population_count/gpw_pop.asc', 'r') as f:
        for i in range(6):
            f.readline() # skip pre data

        for rn in range(4320):
            k = f.readline().split(' ')
            for c in range(8640):
                cell_val = float(k[c]) # read population in grid

                if cell_val < 0: # skip pixel if no population
                    continue

                pixel_map[c, rn] = (0, 0, 0, 100)
                # set pixel at current location to minimum gray
                # square root population to fit within spectrum

init_map(pixel_map)
img.save('map.png')