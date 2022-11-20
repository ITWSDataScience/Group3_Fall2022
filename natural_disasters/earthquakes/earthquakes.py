import csv
from PIL import Image

img = Image.new('RGBA', [8640, 4320], (0, 0, 0, 0))
pixel_map = img.load()

earthquake_color = (255, 0, 0)

def lattopx(lat, height):
    adjlat = -lat + 90
    return adjlat / 180 * height

def longtopx(long, width):
    adjlong = long + 180
    return adjlong / 360 * width

def marker(pixel_map, x, y):
    for i in range(7):
        k = i - 3
        if x + k >= 0 and y - k >= 0 and x + k < 4320 and y - k < 8640: 
            pixel_map[y - k, x + k] = earthquake_color
        if x - k >= 0 and y - k >= 0 and x - k < 4320 and y - k < 8640: 
            pixel_map[y - k, x - k] = earthquake_color

    for i in range(6):
        k = i - 2
        if x + k >= 0 and y - k + 1 >= 0 and x + k < 4320 and y - k + 1 < 8640: 
            pixel_map[y - k + 1, x + k] = earthquake_color
        if x + k - 1 >= 0 and y - k >= 0 and x + k - 1 < 4320 and y - k < 8640: 
            pixel_map[y - k, x + k - 1] = earthquake_color
        if x - k + 1 >= 0 and y - k >= 0 and x - k + 1 < 4320 and y - k < 8640: 
            pixel_map[y - k, x - k + 1] = earthquake_color
        if x - k >= 0 and y - k + 1 >= 0 and x - k < 4320 and y - k + 1 < 8640: 
            pixel_map[y - k + 1, x - k] = earthquake_color

def earthquakes(pixel_map):
    with open('./earthquakes.tsv', 'r') as f:
        eqreader = csv.reader(f, delimiter='\t', quotechar='"')

        i = 0
        for row in eqreader:
            if i < 2:
                i += 1
                continue # skip predata

            lat, long = float(row[10]), float(row[11])
            pxr, pxc = lattopx(lat, 4320), longtopx(long, 8640) # convert coordinates to pixel values

            marker(pixel_map, pxr, pxc)

earthquakes(pixel_map)
img.save('earthquakes.png')