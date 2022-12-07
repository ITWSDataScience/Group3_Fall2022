import netCDF4 as nc
import math
from PIL import Image

img = Image.new('RGBA', [8640, 4320], (0, 0, 0, 0))
pixel_map = img.load()

veg_color = (88, 245, 49)

def lattopx(lat, height):
    adjlat = -lat + 90
    return adjlat / 180 * height

def longtopx(long, width):
    adjlong = long + 180
    return adjlong / 360 * width

def marker(pixel_map, x, y, val):
    for i in range(5):
        for j in range(5):
            if x + j - 2 >= 0 and y + i - 2 >= 0 and x + j - 2 < 4320 and y + i - 2 < 8640:
                pixel_map[y + i - 2, x + j - 2] = veg_color

    for i in range(int(val * 2)):
        for j in range(3):
            if x - i - 3 >= 0 and y + j - 1 >= 0 and x - i - 3 < 4320 and y + j - 1 < 8640:
                pixel_map[y + j - 1, x - i - 3] = veg_color

def vegetation(pixel_map):
    filename = './vegetation.nc'
    ds = nc.Dataset(filename)

    # print(len(ds['M2TMNXFLX_5_12_4_SPEED'][:][0]))

    for r in range(120): 
        for c in range(192):
            rr, cc = 3 * r, 3 * c
            lat, lon = float(ds['lat'][rr]), float(ds['lon'][cc])
            val = float(ds['M2TMNXLND_5_12_4_LAI'][rr][cc])

            if math.isnan(val):
                continue

            rpx, cpx = int(lattopx(lat, 4320)), int(longtopx(lon, 8640))
            
            if rpx == 4320:
                rpx -= 1
            
            if cpx == 8640:
                cpx -= 1

            marker(pixel_map, rpx, cpx, val)

vegetation(pixel_map)
img.save('vegetation.png')