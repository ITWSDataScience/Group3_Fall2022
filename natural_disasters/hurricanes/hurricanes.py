import csv
import math
from PIL import Image

img = Image.new('RGBA', [8640, 4320], (0, 0, 0, 0))
pixel_map = img.load()

hurricane_line = (0, 255, 238)
hurricane_cone = (0, 255, 238, 0.4)

def lattopx(lat, height):
    adjlat = -lat + 90
    return adjlat / 180 * height

def longtopx(long, width):
    adjlong = long + 180
    return adjlong / 360 * width

def latsize(lat, height):
    return (lat / 180) * height

def lonsize(long, width):
    return (long / 360) * width

def readlat(lat):
    if lat[-1] == 'N':
        return float(lat[:-1])
    else:
        return -float(lat[:-1])

def readlon(lon):
    if lon[-1] == 'W':
        return -float(lon[:-1])
    else:
        return float(lon[:-1])

def sanity_check(hurricanepath):
    for p in range(len(hurricanepath) - 1):
        pxr1 = int(hurricanepath[p][0])
        pxc1 = int(hurricanepath[p][1])

        pxr2 = int(hurricanepath[p+1][0])
        pxc2 = int(hurricanepath[p+1][1])
        
        if math.sqrt((pxr2 - pxr1) ** 2 + (pxc2 - pxc1) ** 2) > 200:
            return False
    return True

def marker(pixel_map, hurricanepath):
    for p in range(len(hurricanepath) - 1):
        pxr1 = int(hurricanepath[p][0])
        pxc1 = int(hurricanepath[p][1])

        pxr2 = int(hurricanepath[p+1][0])
        pxc2 = int(hurricanepath[p+1][1])

        latwidth = hurricanepath[p][2]
        longwidth = hurricanepath[p][3]

        if (pxc2 - pxc1) == 0:
            slope = 'inf'
        else:
            slope = (pxr2 - pxr1) / (pxc2 - pxc1)
            inter = pxr1 - slope * pxc1

        if slope == 'inf':
            for i in range(min(pxr1, pxr2), max(pxr1, pxr2)):
                if i < 4320 and i >= 0 and pxc1 < 8640 and pxc1 >= 0:
                    pixel_map[pxc1, i] = hurricane_line
        else:
            for i in range(min(pxr1, pxr2), max(pxr1, pxr2)):
                for j in range(min(pxc1, pxc2), max(pxc1, pxc2)):
                    if abs(int(round(j * slope + inter) - i)) < 2:
                        if j < 8640 and i < 4320 and j >= 0 and i >= 0:
                            pixel_map[j, i] = hurricane_line

def hurricanes(pixel_map):
    years = [str(i) for i in range(2012, 2022)]

    with open('./hurricanes.csv', 'r') as f:
        eqreader = csv.reader(f, delimiter=',', quotechar='"')

        i = 0
        currhurricane = []
        landfall = False
        currname = ''
        for row in eqreader:
            if i < 2:
                i += 1
                continue # skip predata

            if currname != row[5]:
                if landfall and sanity_check(currhurricane):
                    marker(pixel_map, currhurricane)
                currhurricane = []
                currname = row[5]
                landfall = False

            if int(row[1]) < 2012:
                continue

            # lat is row[4], long is row[5]
            # 50kt 84, 85, 86, 87

            fiftyktdata = [
                [30, 31, 32, 33],
                [48, 49],
                [84, 85, 86, 87],
                [104, 105, 106, 107]
            ]

            ctns = []

            for k in fiftyktdata:
                b = False
                for i in k:
                    if row[i].strip() == '':
                        b = True

                if b:
                    continue
                ctns = [float(row[i]) for i in k]
                break

            lat, long = float(row[8]), float(row[9])
            pxr, pxc = lattopx(lat, 4320), longtopx(long, 8640) # convert coordinates to pixel values

            # 1 degree of latitude is 60 nautical miles
            # 1 degree of longitude is 60 nautical miles * cos(latitude)

            # avgrad = sum(ctns) / len(ctns)

            # latwidth = latsize(avgrad / 60, 8640)
            # longwidth = lonsize(avgrad / 60 * abs(math.cos(math.radians(lat))), 4320)

            currhurricane.append((pxr, pxc, 0, 0))

            if row[15].strip() != '' and int(row[15]) == 0:
                landfall = True

hurricanes(pixel_map)
img.save('./hurricanes.png')