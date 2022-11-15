import math

# population map max is 1710353
# scale other pixels accordingly

def population(pixel_map):
    with open('./population_count/gpw_pop.asc', 'r') as f:
        for i in range(6):
            f.readline() # skip pre data

        for rn in range(4320):
            k = f.readline().split(' ')
            for c in range(8640):
                cell_val = float(k[c]) # read population in grid

                if cell_val < 0: # skip pixel if no population
                    continue

                pixel_map[c, rn] = (30, int(math.sqrt(cell_val) * 0.5 + 30), 30)
                # set pixel at current location to minimum gray + green based on population level
                # square root population to fit within spectrum