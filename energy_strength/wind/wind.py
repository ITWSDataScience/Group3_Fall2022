import netCDF4 as nc
import sys
import numpy

wind_color = (71,142,255)

def lattopx(lat, height):
    adjlat = -lat + 90
    return adjlat / 180 * height

def longtopx(long, width):
    adjlong = long + 180
    return adjlong / 360 * width

def marker(pixel_map, x, y, val):
    for i in range(5):
        for j in range(5):
            pixel_map[y + i - 2, x + j - 2] = wind_color
    
    for i in range(int(val)):
        for j in range(3):
            pixel_map[y + i + 3, x + j - 1] = wind_color

def wind(pixel_map):
    filename = './energy_strength/wind/avg_wind_speed.nc'
    ds = nc.Dataset(filename)

    # print(len(ds['M2TMNXFLX_5_12_4_SPEED'][:][0]))

    for r in range(120): 
        for c in range(192):
            rr, cc = 3 * r, 3 * c
            lat, lon = float(ds['lat'][rr]), float(ds['lon'][cc])
            val = float(ds['M2TMNXFLX_5_12_4_SPEED'][rr][cc])

            rpx, cpx = int(lattopx(lat, 4320)), int(longtopx(lon, 8640))
            
            if rpx == 4320:
                rpx -= 1
            
            if cpx == 8640:
                cpx -= 1

            if pixel_map[cpx, rpx] != (0,0,0) and pixel_map[cpx, rpx] != (255,0,0):
                marker(pixel_map, rpx, cpx, val)