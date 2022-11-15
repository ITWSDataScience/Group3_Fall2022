import csv

def lattopx(lat, height):
    adjlat = -lat + 90
    return adjlat / 180 * height

def longtopx(long, width):
    adjlong = long + 180
    return adjlong / 360 * width

def marker(pixel_map, x, y):
    for i in range(7):
        k = i - 3
        pixel_map[y - k, x + k] = (255, 0, 0)
        pixel_map[y - k, x - k] = (255, 0, 0)

    for i in range(6):
        k = i - 2
        pixel_map[y - k + 1, x + k] = (255, 0, 0)
        pixel_map[y - k, x + k - 1] = (255, 0, 0)
        pixel_map[y - k, x - k + 1] = (255, 0, 0)
        pixel_map[y - k + 1, x - k] = (255, 0, 0)

def earthquakes(pixel_map):
    with open('./natural_disasters/earthquakes/earthquakes.tsv', 'r') as f:
        eqreader = csv.reader(f, delimiter='\t', quotechar='"')

        i = 0
        for row in eqreader:
            if i < 2:
                i += 1
                continue # skip predata

            lat, long = float(row[10]), float(row[11])
            pxr, pxc = lattopx(lat, 4320), longtopx(long, 8640) # convert coordinates to pixel values

            marker(pixel_map, pxr, pxc)