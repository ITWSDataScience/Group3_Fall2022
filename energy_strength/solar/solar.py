import netCDF4 as nc
from PIL import Image
import math

img = Image.new('RGBA', [8640, 4320], (0, 0, 0, 0))
pixel_map = img.load()

solar_color = (201, 20, 20)

def lattopx(lat, height):
    adjlat = -lat + 90
    return adjlat / 180 * height

def longtopx(long, width):
    adjlong = long + 180
    return adjlong / 360 * width

def marker(pixel_map, x, y, val):
    val /= 25

    for i in range(5):
        for j in range(5):
            if x + j - 2 >= 0 and y + i - 2 >= 0 and x + j - 2 < 4320 and y + i - 2 < 8640:
                pixel_map[y + i - 2, x + j - 2] = solar_color
    
    for i in range(int(val)):
        for j in range(3):
            if x + j - 1 >= 0 and y + i + 3 >= 0 and x + j - 1 < 4320 and y + i + 3 < 8640:
                pixel_map[y + i + 3, x + j - 1] = solar_color

def solar(pixel_map):
    filename = './avg_solar_energy.nc'
    ds = nc.Dataset(filename)

    # print(ds['FLDAS_NOAH01_CP_GL_M_001_SWdown_f_tavg'][:][0][0])

    # max c = 3600
    # max r = 1500

    for r in range(125): 
        for c in range(200):
            rr, cc = 12 * r, 18 * c
            lat, lon = float(ds['lat'][rr]), float(ds['lon'][cc])
            val = float(ds['FLDAS_NOAH01_CP_GL_M_001_SWdown_f_tavg'][rr][cc])

            if math.isnan(val):
                continue;

            rpx, cpx = int(lattopx(lat, 4320)), int(longtopx(lon, 8640))
            
            if rpx == 4320:
                rpx -= 1
            
            if cpx == 8640:
                cpx -= 1

            marker(pixel_map, rpx, cpx, val)

solar(pixel_map)
img.save('solar.png')