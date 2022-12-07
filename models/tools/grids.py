def lattopx(lat, height):
    adjlat = -lat + 90
    return (adjlat / 180) * height

def longtopx(long, width):
    adjlong = long + 180
    return (adjlong / 360) * width


# Gets long and lat from pixels
def pxtolong(px):
    width = 8640
    adjlong = (px / width) * 360 
    return adjlong - 180

def pxtolat(px):
    height = 4320
    adjlat = (px/height) * 180
    return -(adjlat -90)